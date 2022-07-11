from werkzeug.http import HTTP_STATUS_CODES
import json, random, string, secrets
from flask import make_response, jsonify, g, current_app, request, abort
from functools import wraps
from db.db_config import *
import jwt

JSON_MIME_TYPE = 'application/json; charset=utf-8'
STATUS = 'success'


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)


def error_response(error, message=''):
    error = json.dumps({'status': 'failed',
                        'message': message,
                        'error': error})
    return json_response(error)


def success_response(result, message=''):
    format = {'status': 'success',
                  'message': message,
                  'result': result}
    return json_response(json.dumps(format))


def success_message(message):
    format = {'status': 'success',
              'result': message}

    return json_response(json.dumps(format))

def temp_passwd(num=14):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))


def api_abort(code, message=None, **kwargs):
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')

    response = jsonify(code=code, message=message, **kwargs)
    response.status_code = code
    return response

def get_token():
    if 'Authorization' in request.headers:
        try:
            token_type, token = request.headers['Authorization'].split(None, 1)
        except ValueError:
            token_type = token = None
    else:
        token_type = token = None

    return token_type, token

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_type, token = get_token()
        if request.method != 'OPTIONS':
            if token_type is None or token_type.lower() != 'bearer':
                return abort(400, 'The token type must be bearer.')
            if token is None:
                return token_missing()
            if not validate_token(token):
                return invalid_token()
        return f(*args, **kwargs)

    return decorated


def invalid_token():
    response = api_abort(401, error='invalid_token', error_description='Either the token was expired or invalid.')
    response.headers['WWW-Authenticate'] = 'Bearer'
    return response

def token_missing():
    response = api_abort(401)
    response.headers['WWW-Authenticate'] = 'Bearer'
    return response

def validate_token(token):
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    user = Uzytkownik.query.filter_by(token=data['token']).first()
    g.current_user = user
    return True