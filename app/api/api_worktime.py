from datetime import datetime, timedelta
from flask import request
from utils.uitils import *
from db.db_config import *
from credentials import SENDGRID_API_KEY
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

working_times_schema = Czas_pracySchema(many=True)
working_time_schema = Czas_pracySchema()
break_times_schema = Przerwa_kelnerskaSchema(many=True)
break_time_schema = Przerwa_kelnerskaSchema()
holiday_schema = Urlop_pracySchema()
holidays_schema = Urlop_pracySchema(many=True)

# Nieobecność. (email do managera)
def add_unavailability_api():
    if request.method == 'POST':
        try:
            data = request.get_json()
            start_date = datetime.strptime(data['startDate'], '%Y-%m-%d')
            end_date = datetime.strptime(data['endDate'], '%Y-%m-%d')
            if start_date <= end_date:
                if data['reason'] and data['reason'] != '':
                    return email_to_manager(data['username'], start_date, end_date, 'unavailability', data['reason'] )
                else:
                    return email_to_manager(data['username'], start_date, end_date, 'unavailability')
            else:
                return error_response("The end date cannot be less than the start date"), 400
        except Exception as e:
            return error_response(e), 400

def holiday_api(id = None):
# Wyświetl urlopy (id pracownika).
    if request.method == 'GET':
        if id == None:
            holiday = Urlop_pracy.query.all()
            result = holidays_schema.dump(holiday)
            return success_response(result, f"Urlopy")
        elif id:
            user = Uzytkownik.query.filter_by(username=id).first()
            holiday = Urlop_pracy.query.filter_by(workerId=user.id).all()
            result = holidays_schema.dump(holiday)
            return success_response(result, f"Vacations of employee {user.firstName} {user.lastName}"), 200
        else:
            return error_response("Error while downloading leave"), 400
# Dodaj prośbę o urlop
    if request.method == 'PUT':
        data = request.get_json()
        user = Uzytkownik.query.filter_by(username=data['username']).first()
        timeStart = datetime.strptime(data['timeStart'], '%Y-%m-%d')
        timeEnd = datetime.strptime(data['timeEnd'], '%Y-%m-%d')
        if timeStart <= timeEnd:
            holiday = Urlop_pracy()
            holiday.workerId = user.id
            holiday.timeStart = timeStart
            holiday.timeEnd = timeEnd
            holiday.status = 'waiting'
            holiday.reason = data['reason']
            db.session.add(holiday)
            db.session.commit()
            holiday = Urlop_pracy.query.order_by(Urlop_pracy.id.desc()).first()
            result = holiday_schema.dump(holiday)
            return email_to_manager(data['username'], holiday.timeStart, holiday.timeStart, 'holiday', holiday.reason, holiday.id)
# Rozważ prośbę pracownika o urlop.
    if request.method == 'PATCH':
        data = request.get_json()
        holiday = Urlop_pracy.query.filter_by(id=id).first()
        holiday.status = data['status']
        db.session.commit()
        holiday = Urlop_pracy.query.filter_by(id=id).first()
        result = holiday_schema.dump(holiday)
        return email_to_user(holiday.workerId, holiday.timeStart, holiday.timeEnd, holiday.status, holiday.id)
# Usuwanie urlopu.
    if request.method == 'DELETE':
        holiday = Urlop_pracy.query.filter_by(id=id).first()
        result = holiday_schema.dump(holiday)
        db.session.delete(holiday)
        db.session.commit()
        return success_response(result, f"Vacation has been removed"), 200


def worktime_api(id = None):
# Wyświetl czas pracy (id pracownika).
    if request.method == 'GET':
        if id:
            user = Uzytkownik.query.filter_by(username=id).first()
            working_time = Czas_pracy.query.filter_by(waiterId=user.id).all()
            result = working_times_schema.dump(working_time)
            return success_response(result, f"Employee work time {user.firstName} {user.lastName}"), 200
        else:
            return error_response("Error while downloading working time"), 400
# Dodaj czas pracy. (poczętek i koniec + id pracownika)
    if request.method == 'PUT':
        data = request.get_json()
        user = Uzytkownik.query.filter_by(username=data['username']).first()
        timeStart = datetime.strptime(data['timeStart'], '%Y-%m-%dT%H:%M:%S.%f')
        timeEnd = datetime.strptime(data['timeEnd'], '%Y-%m-%dT%H:%M:%S.%f')
        if timeStart < timeEnd:
            working_time = Czas_pracy(
                waiterId=user.id,
                timeStart = timeStart,
                timeEnd = timeEnd
            )
            db.session.add(working_time)
            db.session.commit()
            result = {
                "username": user.username,
                "id": working_time.id,
                "timeStart": data['timeStart'],
                "timeEnd": data['timeEnd']
            }
            return success_response(result, f"Employee work time {user.firstName} {user.lastName} has been added"), 201
        else:
            return error_response("The start date of the work cannot be later than the end date"), 400
# Edytuj czas pracy (id pracownika).
    if request.method == 'PATCH':
        data = request.get_json()
        user = Uzytkownik.query.filter_by(username=data['username']).first()
        if data['timeStart'] < data['timeEnd']:
            working_time = Czas_pracy.query.filter_by(id=id).first()
            if 'timeStart' in data:
                working_time.timeStart = datetime.strptime(data['timeStart'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'timeEnd' in data:
                working_time.timeEnd = datetime.strptime(data['timeEnd'], '%Y-%m-%dT%H:%M:%S.%f')
            db.session.commit()
            working_time = Czas_pracy.query.filter_by(id=id).first()
            result = {
                'username': user.username,
                'id_working_time': working_time.id,
                'timeStart': working_time.timeStart.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                'timeEnd': working_time.timeEnd.strftime('%Y-%m-%dT%H:%M:%S.%f')
            }
            return success_response(result, f"Working hours have been updated"), 200
        else:
            return error_response("Error while adding working time"), 400
# Usuń czas pracy (id pracownika).
    if request.method == 'DELETE':
        working_time = Czas_pracy.query.filter_by(id=id).first()
        result = working_time_schema.dump(working_time)
        db.session.delete(working_time)
        db.session.commit()
        return success_response(result, f"Working time has been removed"), 200

# Dodawanie, edycja i usuwanie wartości przerwy kelnerskiej. (int czas w minutach)
def breaktime_api(id=None):
    if request.method == 'PUT':
        data = request.get_json()
        break_time = Przerwa_kelnerska(time=data['time'])
        db.session.add(break_time)
        db.session.commit()
        break_time = Przerwa_kelnerska.query.order_by(Przerwa_kelnerska.id.desc()).first()
        result = break_time_schema.dump(break_time)
        return success_response(result, f"A waiter break of {data['time']} minutes has been added"), 201
    if request.method == 'GET':
        break_time = Przerwa_kelnerska.query.all()
        result = break_times_schema.dump(break_time)
        return success_response(result, f"Waiter breaks")
    if request.method == 'PATCH':
        data = request.get_json()
        break_time = Przerwa_kelnerska.query.filter_by(id=id).first()
        break_time.time = data['time']
        db.session.commit()
        break_time = Przerwa_kelnerska.query.filter_by(id=id).first()
        result = break_time_schema.dump(break_time)
        return success_response(result, f"Waiter's break has been updated")
    if request.method == 'DELETE':
        break_time = Przerwa_kelnerska.query.filter_by(id=id).first()
        result = break_time_schema.dump(break_time)
        db.session.delete(break_time)
        db.session.commit()
        return success_response(result, f"The waitressing break has been removed")

# Mail z inforamcją o nieobecności do managera.
def email_to_manager(user_id, start_date, end_date, option, reason="Nie podano powodu", idUrlop = None):
    
    user = Uzytkownik.query.filter_by(username=user_id).first()
    manager = Uzytkownik.query.filter_by(role='manager').first()
    message = Mail()
    if user and manager:
# email z informajcją o nieobecności do managera.
        if option == 'unavailability':
            message.from_email = From(
                email='notifier@smtp.gastrocrm.online', 
                name='GastroCRM', 
                p=True
            )
            message.to = To(email=manager.email)
            message.subject = Subject(f'{user.firstName} zgłasza niedostępność - GastroCRM')
            if start_date == end_date:
                message.content = [
                Content(
                    mime_type="text/html", 
                    content=f'Witaj {manager.firstName}!<br /><br />Pracownik {user.firstName} {user.lastName} informuje że nie będzie dostępny w dniu {start_date}<br /><br />Powód:<br />{reason}<br /><br />GastroCRM'
                )
            ]
            else:
                message.content = [
                    Content(
                        mime_type="text/html", 
                        content=f'Witaj {manager.firstName}!<br /><br />Pracownik {user.firstName} {user.lastName} informuje że nie będzie dostępny w dniach {start_date} do {end_date}<br /><br />Powód:<br />{reason}<br /><br />GastroCRM'
                    )
                ]
# emai z informacją wniosku o urlop
        if option == 'holiday':
            message.from_email = From(
                email='notifier@smtp.gastrocrm.online', 
                name='GastroCRM', 
                p=True
            )
            message.to = To(email=manager.email)
            message.subject = Subject(f'{user.firstName} złożył wniosek o urlop - GastroCRM')
            if start_date == end_date:
                message.content = [
                    Content(
                        mime_type="text/html", 
                        content=f'Witaj {manager.firstName}!<br /><br />Pracownik {user.firstName} {user.lastName} złożył wniosek o urlop w dniu {start_date}<br /><br />Powód: {reason}<br /><br />Wniosek możesz zobaczyć w swoim GastroCRM w zakładce <strong>Urlopy</strong> <br /><br />GastroCRM'
                    )
                ]
            else:
                message.content = [
                    Content(
                        mime_type="text/html", 
                        content=f'Witaj {manager.firstName}!<br /><br />Pracownik {user.firstName} {user.lastName} złożył wniosek o urlop w dniach {start_date} do {end_date}<br /><br />Powód: {reason}<br /><br />Wniosek możesz zobaczyć w swoim GastroCRM w zakładce <strong>Urlopy</strong> <br /><br />GastroCRM'
                    )
                ]
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        if idUrlop != None:
            result = {
                'idUrlop': idUrlop,
                'username': user.username,
                'manager': manager.username,
                'manager_email': manager.email,
            }
        else:
            result = {
                'username': user.username,
                'manager': manager.username,
                'manager_email': manager.email,
            }
        if user and manager:
            if option == 'unavailability':
                return success_response(result, f"A message was sent to {manager.firstName} {manager.lastName} about the absence"), 200
            if option == 'holiday':
                return success_response(result, f"Leave has been added, A message has been sent to {manager.firstName} {manager.lastName} about the leave"), 200
        else:
            return error_response("Error while sending an email"), 500
    except Exception as e:
        return error_response(str(e)), 400

# Mail z inforamcją o stausie wniokslu urlopowego.
def email_to_user(user_id, start_date, end_date, status, idUrlop):
    
    user = Uzytkownik.query.filter_by(id=user_id).first()
    message = Mail()
    if user :
        message.from_email = From(
            email='notifier@smtp.gastrocrm.online', 
            name='GastroCRM', 
            p=True
        )
        message.to = To(email=user.email)
        message.subject = Subject(f'{user.firstName} wniosek o urlop został zaakceptowany - GastroCRM')
        if start_date == end_date:
            message.content = [
            Content(
                mime_type="text/html", 
                content=f'Witaj {user.firstName}!<br /><br />Złożony przez ciebie wniosek o urlop w dniu {start_date} zmienił status na: <strong>{status}</strong><br /><br />Wniosek możesz zobaczyć w swoim GastroCRM w zakładce <strong>Urlopy</strong> <br /><br />GastroCRM'
            )
        ]
        else:
            message.content = [
                Content(
                    mime_type="text/html", 
                    content=f'Witaj {user.firstName}!<br /><br />Złożony przez ciebie wniosek o urlop w dniach {start_date} do {end_date} zmienił status na: <strong>{status}</strong><br /><br />Wniosek możesz zobaczyć w swoim GastroCRM w zakładce <strong>Urlopy</strong> <br /><br />GastroCRM'
                )
            ]
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        result = {
            'username': user.username,
            'email': user.email,
            'send_code': response.status_code,
        }
        if user:
            return success_response(result, f"The request status has been changed and a message has been sent to the requester {user.firstName} {user.lastName}"), 200
        else:
            return error_response("Error while sending an email"), 500
    except Exception as e:
        return error_response(str(e)), 400