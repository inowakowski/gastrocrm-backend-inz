from flask import request, Flask
import uuid
from utils.uitils import *
import random, string, secrets
from db.db_config import *
from datetime import datetime, timedelta

working_time_schema = Czas_pracySchema(many=True)
work_time_schema = Czas_pracySchema()


# Wyświetl statystyki sprzedaży.
# Show statistics of sales
def show_statistics_sales():
    if request.method == "POST":
        try:
            data = request.get_json()
            statistics_sales = []
            summary_sales=0
            if data == None or data == {} or data == [] or data == '':
                ordered_dishes = Zamowienie.query.all()
                for dishes in ordered_dishes:
                    dish_sales = Zamowienie_produkty.query.filter_by(orderId=dishes.id).all()
                    sales = 0
                    quantity = 0
                    orders = []
                    for dish in dish_sales:
                        dish_price = Potrawa.query.filter_by(id=dish.dishId).first()
                        sales += dish_price.price
                        quantity += 1
                        res = {
                            'disheId': dish.dishId,
                            'dishName': dish_price.name,
                            'dishPrice': dish_price.price,
                        }
                        orders.append(res)
                    result = {
                        'orderId': dishes.id,
                        'tableNumber': dishes.tableNumber,
                        'status': dishes.status,
                        'totalSales': sales,
                        'orders': orders
                    }
                    summary_sales += sales
                    statistics_sales.append(result)
                result_final = {
                    'waiterSummarySales': summary_sales,
                    'sales':statistics_sales
                }
                return success_response(result_final, 'Statistics sales'), 200
            elif data['from'] and data['to']:
                if data['from'] > data['to']:
                    return error_response("Start time is greater than end time")
                else:
                    start_date = datetime.strptime(data['from'], '%Y-%m-%d')
                    end_date = datetime.strptime(data['to'], '%Y-%m-%d')
                    ordered_dishes = Zamowienie.query.filter(Zamowienie.orderDate >= start_date).filter(Zamowienie.orderDate <= end_date).all()
                    for dishes in ordered_dishes:
                        dish_sales = Zamowienie_produkty.query.filter_by(orderId=dishes.id)
                        sales = 0
                        quantity = 0
                        result = {}
                        orders = []
                        for dish in dish_sales:
                            dish_price = Potrawa.query.filter_by(id=dish.dishId).first()
                            sales += dish_price.price
                            quantity += 1
                            res = {
                                'disheId': dish.dishId,
                                'dishName': dish_price.name,
                                'dishPrice': dish_price.price,
                            }
                            orders.append(res)
                        result = {
                            'orderId': dishes.id,
                            'tableNumber': dishes.tableNumber,
                            'status': dishes.status,
                            'totalSales': sales,
                            'orders': orders
                        }
                        summary_sales += sales
                        statistics_sales.append(result)
                    result_final = {
                        'waiterSummarySales': summary_sales,
                        'sales':statistics_sales
                    }
                    return success_response(result_final, f'Statistics sales from {data["from"]} to {data["to"]}'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Wyświetl statystyki czasu pracy wszystkich pracowników.
def show_statistics_time(id=None):
    if request.method == "POST":
        try:
            data = request.get_json()
            statistics_time = []
            if id == None:
                users = Uzytkownik.query.all()
                if data == None or data == {} or data == [] or data == '':
                    for user in users:
                        worker_time = Czas_pracy.query.filter_by(waiterId=user.id).all()
                        summary_work_time = timedelta(0)
                        for time in worker_time:
                            times = work_time_schema.dump(time)
                            timeStart = datetime.strptime(times['timeStart'], '%Y-%m-%dT%H:%M:%S')
                            timeEnd = datetime.strptime(times['timeEnd'], '%Y-%m-%dT%H:%M:%S')
                            _work_time = timeEnd - timeStart
                            summary_work_time += _work_time
                        work_time_hours = summary_work_time.seconds // 3600 + summary_work_time.days * 24
                        work_time_minutes = (summary_work_time.seconds // 60) % 60 
                        if work_time_minutes < 10:
                            work_time_minutes = f'0{work_time_minutes}'
                        work_time_seconds = summary_work_time.seconds % 60
                        if work_time_seconds < 10:
                            work_time_seconds = f'0{work_time_seconds}'
                        work_time = f'{work_time_hours}:{work_time_minutes}:{work_time_seconds}'
                        result = {
                            'userId': user.id,
                            'username': user.username,
                            'firstName': user.firstName,
                            'lastName': user.lastName,
                            'worktime': str(work_time),
                        }
                        statistics_time.append(result)
                    return success_response(statistics_time, 'Statistics work time'), 200
                elif data['from'] and data['to']:
                    if data['from'] > data['to']:
                        return error_response("Start time is greater than end time"), 400
                    else:
                        start_date = datetime.strptime(data['from'], '%Y-%m-%d')
                        end_date = datetime.strptime(data['to'], '%Y-%m-%d')
                        for user in users:
                            worker_time = Czas_pracy.query.filter_by(waiterId=user.id).filter(Czas_pracy.timeStart >= start_date).filter(Czas_pracy.timeEnd <= end_date).all()
                            summary_work_time = timedelta(0)
                            for time in worker_time:
                                times = work_time_schema.dump(time) 
                                timeStart = datetime.strptime(times['timeStart'], '%Y-%m-%dT%H:%M:%S')
                                # timeEnd = datetime.strptime(time.timimeStart, '%Y-%m-%dT%H:%M:%S')
                                timeEnd = datetime.strptime(times['timeEnd'], '%Y-%m-%dT%H:%M:%S')
                                # timeEnd = datetime.strptime(times.timeEnd, '%Y-%m-%dT%H:%M:%S')
                                _work_time = timeEnd - timeStart
                                summary_work_time += _work_time
                            work_time_hours = summary_work_time.seconds // 3600 + summary_work_time.days * 24
                            work_time_minutes = (summary_work_time.seconds // 60) % 60 
                            if work_time_minutes < 10:
                                work_time_minutes = f'0{work_time_minutes}'
                            work_time_seconds = summary_work_time.seconds % 60
                            if work_time_seconds < 10:
                                work_time_seconds = f'0{work_time_seconds}'
                            work_time = f'{work_time_hours}:{work_time_minutes}:{work_time_seconds}'
                            result = {
                                'userId': user.id,
                                'username': user.username,
                                'firstName': user.firstName,
                                'lastName': user.lastName,
                                'worktime': str(work_time),
                            }
                            statistics_time.append(result)
                        return success_response(statistics_time, f'Statistics work time from {data["from"]} to {data["to"]}'), 200
            else:
                user = Uzytkownik.query.filter_by(id=id).first()
                if data == None or data == {} or data == [] or data == '':
                    worker_time = Czas_pracy.query.filter_by(waiterId=user.id).all()
                    summary_work_time = timedelta(0)
                    for time in worker_time:
                        # times = work_time_schema.dump(time)
                        # timeStart = datetime.strptime(times['timeStart'], '%Y-%m-%dT%H:%M:%S')
                        # timeEnd = datetime.strptime(times['timeEnd'], '%Y-%m-%dT%H:%M:%S')
                        # _work_time = timeEnd - timeStart
                        _work_time = time.timeEnd - time.timeStart
                        summary_work_time += _work_time
                    work_time_hours = summary_work_time.seconds // 3600 + summary_work_time.days * 24
                    work_time_minutes = (summary_work_time.seconds // 60) % 60 
                    if work_time_minutes < 10:
                        work_time_minutes = f'0{work_time_minutes}'
                    work_time_seconds = summary_work_time.seconds % 60
                    if work_time_seconds < 10:
                        work_time_seconds = f'0{work_time_seconds}'
                    work_time = f'{work_time_hours}:{work_time_minutes}:{work_time_seconds}'
                    result = {
                        'userId': user.id,
                        'username': user.username,
                        'firstName': user.firstName,
                        'lastName': user.lastName,
                        'worktime': str(work_time),
                    }
                    statistics_time.append(result)
                    return success_response(statistics_time, 'Statistics work time'), 200
                elif data['from'] and data['to']:
                    if data['from'] > data['to']:
                        return error_response("Start time is greater than end time"), 400
                    else:
                        start_date = datetime.strptime(data['from'], '%Y-%m-%d')
                        end_date = datetime.strptime(data['to'], '%Y-%m-%d')
                    worker_time = Czas_pracy.query.filter_by(waiterId=user.id).filter(Czas_pracy.timeStart >= start_date).filter(Czas_pracy.timeEnd <= end_date).all()
                    summary_work_time = timedelta(0)
                    for time in worker_time:
                        # times = work_time_schema.dump(time)
                        # timeStart = datetime.strptime(times['timeStart'], '%Y-%m-%dT%H:%M:%S')
                        # timeEnd = datetime.strptime(times['timeEnd'], '%Y-%m-%dT%H:%M:%S')
                        _work_time = time.timeEnd - time.timeStart
                        summary_work_time += _work_time
                    work_time_hours = summary_work_time.seconds // 3600 + summary_work_time.days * 24
                    work_time_minutes = (summary_work_time.seconds // 60) % 60 
                    if work_time_minutes < 10:
                        work_time_minutes = f'0{work_time_minutes}'
                    work_time_seconds = summary_work_time.seconds % 60
                    if work_time_seconds < 10:
                        work_time_seconds = f'0{work_time_seconds}'
                    work_time = f'{work_time_hours}:{work_time_minutes}:{work_time_seconds}'
                    result = {
                        'userId': user.id,
                        'username': user.username,
                        'firstName': user.firstName,
                        'lastName': user.lastName,
                        'worktime': str(work_time),
                    }
                    statistics_time.append(result)
                    return success_response(statistics_time, f'Statistics work time from {data["from"]} to {data["to"]}'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Wyświetl statystyki miesięczne sprzedaży kelnera
def show_waiter_sale_statistics(id):
    if request.method == "POST":
        try:
            data = request.get_json()
            user = Uzytkownik.query.filter_by(id=id).first()
            statistics_sales = []
            summary_sales=0
            if data == None or data == {} or data == [] or data == '':
                ordered_dishes = Zamowienie.query.filter_by(waiterId=id).all()
                for dishes in ordered_dishes:
                    dish_sales = Zamowienie_produkty.query.filter_by(orderId=dishes.id).all()
                    sales = 0
                    quantity = 0
                    orders = []
                    for dish in dish_sales:
                        dish_price = Potrawa.query.filter_by(id=dish.dishId).first()
                        sales += dish_price.price
                        quantity += 1
                        res = {
                            'disheId': dish.dishId,
                            'dishName': dish_price.name,
                            'dishPrice': dish_price.price,
                        }
                        orders.append(res)
                    result = {
                        'orderId': dishes.id,
                        'tableNumber': dishes.tableNumber,
                        'status': dishes.status,
                        'totalSales': sales,
                        'orders': orders
                    }
                    summary_sales += sales
                    statistics_sales.append(result)
                result_final = {
                    'summarySales': summary_sales,
                    'sales':statistics_sales
                }
                return success_response(result_final, f'{user.username} waiter\'s sales statistics'), 200
            elif data['from'] and data['to']:
                if data['from'] > data['to']:
                    return error_response("Start time is greater than end time"), 400
                else:
                    start_date = datetime.strptime(data['from'], '%Y-%m-%d')
                    end_date = datetime.strptime(data['to'], '%Y-%m-%d')
                    ordered_dishes = Zamowienie.query.filter_by(waiterId=id).filter(Zamowienie.orderDate >= start_date).filter(Zamowienie.orderDate <= end_date).all()
                    for dishes in ordered_dishes:
                        dish_sales = Zamowienie_produkty.query.filter_by(orderId=dishes.id)
                        sales = 0
                        quantity = 0
                        result = {}
                        orders = []
                        for dish in dish_sales:
                            dish_price = Potrawa.query.filter_by(id=dish.dishId).first()
                            sales += dish_price.price
                            quantity += 1
                            res = {
                                'disheId': dish.dishId,
                                'dishName': dish_price.name,
                                'dishPrice': dish_price.price,
                            }
                            orders.append(res)
                        result = {
                            'orderId': dishes.id,
                            'tableNumber': dishes.tableNumber,
                            'status': dishes.status,
                            'totalSales': sales,
                            'orders': orders
                        }
                        summary_sales += sales
                        statistics_sales.append(result)
                    result_final = {
                        'summarySales': summary_sales,
                        'sales':statistics_sales
                    }
                    return success_response(result_final, f'{user.username} waiter\'s sales statistics from {data["from"]} to {data["to"]}'), 200
        except Exception as e:
            return error_response(str(e)), 400


