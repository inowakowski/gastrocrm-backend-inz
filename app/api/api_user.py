from flask import request
import jwt
import os
from utils.uitils import *
from db.db_config import *
from werkzeug.security import generate_password_hash, check_password_hash
from credentials import SENDGRID_API_KEY
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

user_schema = UzytkownikSchema()
users_schema = UzytkownikSchema(many=True)

#Function to show all users in database
def get_users():
    if request.method == 'GET':
        try:
            users = Uzytkownik.query.all()
            result = users_schema.dump(users)
            return success_response(result, 'User list'), 200
        except Exception as e:
            return error_response(str(e)), 400

#Function to show user profile by role
def get_users_by_role(role):
    if request.method == 'GET':
        try:
            users = Uzytkownik.query.filter_by(role=role).all()
            result = users_schema.dump(users)
            return success_response(result, f'List of users with the role {role}'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Function to show user profile
def get_user(username):
    if request.method == 'GET':
        args = request.args
        if 'username' in args:
            username = args['username']
        try:
            if username.find('@') != -1:
                user = Uzytkownik.query.filter_by(email=username).first()
            elif username.find('@') == -1:
                user = Uzytkownik.query.filter_by(username=username).first()            
            result = user_schema.dump(user)
            return success_response(result, f'Użytkownik {username}'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Function  to log in user
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if "username" in data:
                if data['username'].find('@') != -1:
                    user = Uzytkownik.query.filter_by(email=data['username']).first()
                else:
                    user = Uzytkownik.query.filter_by(username=data['username']).first()

            result = user_schema.dump(user)
            if len(result) == 0:
                return error_response('Incorrect user name or password'), 401
            elif result['tempPassword']:
                return error_response(f'User inactive. Check your email'), 403
            else:
                if check_password_hash(user.password, data['password']):
                    token = jwt.encode({'token' : user.token}, app.config['SECRET_KEY'], algorithm='HS256')
                    res = { 
                        'id': user.id,
                        'firstName': user.firstName,
                        'lastName': user.lastName,
                        'username': user.username,
                        'role': user.role,
                        'token' : token
                    }
                    return success_response(res, f'User logged in {user.username}'), 200
                else:
                    return error_response('Incorrect password'), 401
        except Exception as e:
            return error_response(str(e))

# Function to fprgot password. Send email with temporary password
def forgot_password():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user = Uzytkownik.query.filter_by(email=data['email']).first()
            result = user_schema.dump(user)
            if len(result) == 0:
                return error_response('Invalid email or user does not exist'), 400
            else:
                data = {
                    'firstName': result['firstName'],
                    'email': result['email'],
                    'username': '',
                }
                return temporary_password_send(data, 'forgot')
        except Exception as e:
            return error_response(str(e)), 400

def change_password(username):
    if request.method == 'PATCH':
        try:
            data = request.get_json()
            user = Uzytkownik.query.filter_by(username=username).first()
            result = user_schema.dump(user)
            if len(result) == 0:
                return error_response('Incorrect user name or password'), 400
            else:
                if check_password_hash(user.password, data['password']):
                    hashed_password = generate_password_hash(data['new_password'], method='sha256')
                    Uzytkownik.query.filter_by(username=username).update(dict(password=hashed_password, tempPassword=0))
                    db.session.commit()
                    return success_response([],f'User password {username} has been changed'), 200
        except Exception as e:
            return error_response(str(e)), 400

# add user function
def add_user_api():
    if request.method == 'PUT':
        try:
            data = request.get_json()
            random_password = temp_passwd()
            hashed_password = generate_password_hash(random_password, method='sha256')
            random_token = temp_passwd(32)
            new_user = Uzytkownik()
            if data['role'] == '':
                new_user.role = 'admin'
            else:
                new_user.role = data['role']
            if 'username' in data:
                new_user.username = data['username']
            if 'firstName' in data:
                new_user.firstName = data['firstName']
            if 'lastName' in data:
                new_user.lastName = data['lastName']
            if 'phoneNumber' in data:
                new_user.phoneNumber = data['phoneNumber']
            if 'email' in data:
                if data['email'].find('@') != -1:
                    new_user.email = data['email']
                else:
                    return error_response('Incorrect email'), 400
            new_user.password = hashed_password
            # new_user.tempPassword =
            new_user.tempPassword = 0
            new_user.token = random_token
            db.session.add(new_user)
            db.session.commit()
            return temporary_password_send(data, 'add')
        except Exception as e:
            return error_response(str(e), 'User already exists'), 400
    else:
        return error_response('Incorrect request method'), 400

# edit user function
def edit_user_api(username):
    if request.method == 'PATCH':
        try:
            data = request.get_json()
            user = Uzytkownik.query.filter_by(username=username).first()
            result = user_schema.dump(user)
            if len(result) == 0:
                return error_response('Incorrect user name or password'), 400
            else:
                if 'username' in data:
                    user.username = data['username']
                if 'firstName' in data:
                    user.firstName = data['firstName']
                if 'lastName' in data:
                    user.lastName = data['lastName']
                if 'phoneNumber' in data:
                    user.phoneNumber = data['phoneNumber']
                if 'email' in data:
                    user.email = data['email']
                if 'role' in data:
                    user.role = data['role']
                db.session.commit()
                result = user_schema.dump(user)
                return success_response(result,f'User {username} has been changed'), 200
        except Exception as e:
            return error_response(str(e)), 400

# delete user function
def delete_user_api(username):
    if request.method == 'DELETE':
        try:
            Uzytkownik.query.filter_by(username=username).delete()
            db.session.commit()
            return success_response([],f'User {username} has been deleted'), 200
        except Exception as e:
            return error_response(str(e)), 400
        
# active user function
def active_user_api(username):
    if request.method == 'PATCH':
        try:
            data = request.get_json()
            user = Uzytkownik.query.filter_by(username=username).first()
            result = user_schema.dump(user)
            if len(result) == 0:
                return error_response('Incorrect user name or password'), 400
            else:
                if check_password_hash(user.password, data['password']):
                    Uzytkownik.query.filter_by(username=username).update(dict(tempPassword=0))
                    db.session.commit()
                    return success_response([],f'User {username} has been activated'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Sent email with temporary password
def temporary_password_send(data, option):
    random_password = temp_passwd()
    hashed_password = generate_password_hash(random_password, method='sha256')
    Uzytkownik.query.filter_by(email=data['email']).update(dict(password=hashed_password, tempPassword=0))
    db.session.commit()

    url = "https://gastrocrm.online/"

#email format when user forgot password
    if option == 'forgot':

        message = Mail()
        message.from_email = From(
            email='notifier@smtp.gastrocrm.online', 
            name='GastroCRM', 
            p=True
        )
        message.to = To(email=data['email'])
        message.subject = Subject('Zapomniałeś hasła? - GastroCRM')
        message.content = [
            Content(
                mime_type="text/html", 
                content=f'Witaj {data["firstName"]}!<br /><br />Zapomniałeś hasła?<br /><br />Zostało nadane tobie tymczasowe hasło do logowania to: <strong>{random_password}</strong><br /><br /><h2>Rekomendujemy zmianę hasła po zalogowaniu</h2><br /><br />Kliknij poniżej by przejść do strony logowania<br /><br /><h2><a href={url}>Zaloguj się</h2><br />Pozdrawiamy<br />Zespół GastroCRM'
            )
        ]
# email format for user registration
    elif option == 'add':
        message = Mail()
        message.from_email = From(
            email='notifier@smtp.gastrocrm.online', 
            name='GastroCRM', 
            p=True
        )
        message.to = To(email=data['email'])
        message.subject = Subject(f'Witaj {data["firstName"]}! - GastroCRM')
        message.content = [
            Content(
                mime_type="text/html", 
                content=f'<strong>Witaj {data["firstName"]}!</strong><br /><br />Jako nowemu użytkownikowi zostało Ci nadane tymczasowe hasło do logowania to: <strong>{random_password}</strong><br /><br /><h2>Rekomendujemy zmianę hasła po zalogowaniu</h2><br /><br />Kliknij poniżej by przejść do strony logowania<br /><br /><a href={url}><h2>Zaloguj się</h2></a><br />Pozdrawiamy<br />Zespół GastroCRM'
            )
        ]

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        if os.getenv('ENVIRONMENT', 'development') != 'production':
            result = {
                'email': data['email'],
                'password': random_password
            }
        else:
            result = {
                'email': data['email'],
                'send_code': response.status_code
            }
        if option == 'add':
            return success_response(result,f'User {data["username"]} has been added. A temporary password message was sent to {data["email"]}'), 201
        else:
            return success_response(result,f'A temporary password message was sent to {data["email"]}'), 200
    except Exception as e:
        return error_response(str(e)), 400
