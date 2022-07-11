from datetime import datetime
from unittest import result
from flask import request
from sqlalchemy import desc
from utils.uitils import *
from db.db_config import *

order_schema = ZamowienieSchema()
orders_schema = ZamowienieSchema(many=True)
order_dish_schema = Zamowienie_produktySchema()
orders_dishes_schema = Zamowienie_produktySchema(many=True)
dish_schema = PotrawaSchema()
dishes_schema = PotrawaSchema(many=True)

# Zamówienie. Order.
def get_orders_api(id=None):
    if request.method == "GET":
        try:
            if id is None:
                orders = Zamowienie.query.all()
                result = orders_schema.dump(orders)
                return success_response(result, 'All orders'), 200
            else:
                orders = Zamowienie.query.filter_by(waiterId=id).all()
                result = orders_schema.dump(orders)
                return success_response(result, f'Orders assigned to waiter {id}'), 200
        except Exception as e:
            return error_response(str(e)), 400

def get_order_api(id):
    if request.method == "GET":
        try:
            order = Zamowienie.query.filter_by(id=id).first()
            dishes = Zamowienie_produkty.query.filter_by(orderId=order.id).all()
            result = {
                'order': order_schema.dump(order),
                'dishes': orders_dishes_schema.dump(dishes)
            }
            return success_response(result, 'Order'), 200
        except Exception as e:
            return error_response(str(e)), 400

#Dodaj produkty do zamówienia.
def add_dish_to_order_api():
    if request.method == "PUT":
        try:
            data = request.get_json()
            date = datetime.now()
            check = Zamowienie.query.all()
            if len(check) == 0:
                clientId = 1
            else:
                clientId = check[-1].clientId + 1
            _order = Zamowienie()
            _order.clientId = clientId
            if 'waiterId' in data:
                _order.waiterId = data['waiterId']
            if 'tableNumber' in data:
                _order.tableNumber = data['tableNumber']
            if 'invoice' in data:
                _order.invoice = data['invoice']
            if 'status' in data:
                if data['status'] == 'nowe' or data['status'] == 'Nowa':
                    _order.status = 'new'
                elif data['status'] == 'w realizacji' or data['status'] == 'W realizacji':
                    _order.status = 'in progress'
                elif data['status'] == 'zapłacone' or data['status'] == 'Zapłacone':
                    _order.status = 'paid'
                else:
                    _order.status = 'new'
            else:
                _order.status = 'new'
            _order.orderDate = date.strftime('%Y-%m-%d %H:%M:%S')
            db.session.add(_order)
            db.session.commit()

            order = Zamowienie.query.order_by(Zamowienie.id.desc()).first()

            number = {i:data['orderedDishes'].count(i) for i in data['orderedDishes']}
            dishIds = list(number.keys())
            l_orderedDishes = []

            for ID in dishIds:
                dish = Potrawa.query.filter_by(id=ID).first()
                ordered_dishes = Zamowienie_produkty()
                ordered_dishes.orderId = order.id
                ordered_dishes.dishId = ID
                ordered_dishes.number = number[ID]
                ordered_dishes.price = dish.price
                db.session.add(ordered_dishes)
                db.session.commit()
                ordered_dish = {
                    'dishId': ID,
                    'name': dish.name,
                    'number': ordered_dishes.number,
                    'price_per_dish': dish.price,
                    'price_summary': ordered_dishes.number * dish.price
                }
                l_orderedDishes.append(ordered_dish)


            result = {
                'order': order_schema.dump(order),
                'dishes': l_orderedDishes
            }

            return success_response(result, 'Added product to your order'), 201
        except Exception as e:
            return error_response(str(e)), 400

#Edytuj zamówienie. Edit order.
def edit_order_api(id):
    if request.method == "PATCH":
        try:
            data = request.get_json()
            order = Zamowienie.query.filter_by(id=id).first()
            if 'orderedDishes' in data:
                Zamowienie_produkty.query.filter_by(orderId=id).delete()
                db.session.commit()
            if 'waiterId' in data:
                order.waiterId = data['waiterId']
            if 'tableNumber' in data:
                order.tableNumber = data['tableNumber']
            if 'status' in data:
                if data['status'] == 'nowe' or data['status'] == 'Nowa':
                    _order.status = 'new'
                elif data['status'] == 'w realizacji' or data['status'] == 'W realizacji':
                    _order.status = 'in progress'
                elif data['status'] == 'zapłacone' or data['status'] == 'Zapłacone':
                    _order.status = 'paid'
                else:
                    order.status = data['status']
            db.session.commit()

            number = {i:data['orderedDishes'].count(i) for i in data['orderedDishes']}
            dishIds = list(number.keys())
            l_orderedDishes = []

            for ID in dishIds:
                dish = Potrawa.query.filter_by(id=ID).first()
                ordered_dishes = Zamowienie_produkty()
                ordered_dishes.orderId = id
                ordered_dishes.dishId = ID
                ordered_dishes.number = number[ID]
                ordered_dishes.price = dish.price
                db.session.add(ordered_dishes)
                db.session.commit()
                ordered_dish = {
                    'dishId': ID,
                    'name': dish.name,
                    'number': ordered_dishes.number,
                    'price_per_dish': dish.price,
                    'price_summary': ordered_dishes.number * dish.price
                }
                l_orderedDishes.append(ordered_dish)

            
            result = {
                'order': order_schema.dump(order),
                'dishes': l_orderedDishes
            }

            return success_response(result, 'Order edited'), 200
        except Exception as e:
            return error_response(str(e)), 400


# Podsumuj dane zamówienie.
def summary_order_api(id):
    if request.method == "PATCH":
        try:
            dishes_order = Zamowienie_produkty.query.filter_by(orderId=id).all()
            dishes = []
            for dish in dishes_order:
                _dish = Potrawa.query.filter_by(id=dish.dishId).first()
                dish_data = {
                    'dishId': dish.dishId,
                    'name': _dish.name,
                    'number': dish.number,
                    'price_per_dish': dish.price,
                    'price_summary': dish.number * dish.price
                }
                dishes.append(dish_data)
            summary = 0
            for dish in dishes:
                summary += dish['price_summary']
            
            order = Zamowienie.query.filter_by(id=id).first()
            order.summary = summary
            db.session.commit()

            result = {
                'id': id,
                'summary': summary,
                'dishes': dishes
            }
            return success_response(result, 'Order Summary'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Opłać dane zamówienie.
def pay_order_api(id):
    if request.method == "PATCH":
        try:
#Komunikacja z systemem płatniczym i inforamcja zwrotna o udanej transakcji
            data = request.get_json()
            if data['payment_system_response'] == 'OK':
                order = Zamowienie.query.filter_by(id=id).first()
                Zamowienie.query.filter_by(id=id).update(dict(status='paid'))
                db.session.commit()
                order = Zamowienie.query.filter_by(id=id).first()
                result = order_schema.dump(order)
                return success_response(result, 'The order has been paid'), 200
            else:
                order = Zamowienie.query.filter_by(id=id).first()
                Zamowienie.query.filter_by(id=id).update(dict(status='Payment has failed'))
                db.session.commit()
                order = Zamowienie.query.filter_by(id=id).first()
                result = order_schema.dump(order)
                return error_response(result,'Order has not been paid'), 400
        except Exception as e:
            return error_response(str(e)), 400


# Wystaw fakturę do zamówienia.
def invoice_order_api(id):
    if request.method == "GET":
        try:
            order = Zamowienie.query.filter_by(id=id).first()
            result = order_schema.dump(order)
            if len(result) == 0:
                return error_response(404, 'Order not found'), 404
            else:
                if order.invoice == None:
                    return error_response(404, 'Order has not been invoiced'), 404
                else:
                    return success_response(result, 'Invoice issued'), 200
        except Exception as e:
            return error_response(str(e)), 400
    if request.method == "PATCH":
        try:
            data = request.get_json()
            order = Zamowienie.query.filter_by(id=id).first()
            order.invoice = data['invoice']
            db.session.commit()
            order = Zamowienie.query.filter_by(id=id).first()
            result = order_schema.dump(order)
            return success_response(result, 'I\'m sending an order for invoice, complete with customer information'), 200
        except Exception as e:
            return error_response(str(e)), 400


# Usuń zamówienie. Delete order.
def delete_order_api(id):
    if request.method == "DELETE":
        try:
            dishes = Zamowienie_produkty.query.filter_by(orderId=id).all()
            l_dishes = []
            for dish in dishes:
                single = {
                    'dishId': dish.id,
                    'price': dish.price,
                }
                l_dishes.append(single)
                
            result ={
                'order': order_schema.dump(Zamowienie.query.filter_by(id=id).first()),
                'dishes': l_dishes
            }
            Zamowienie_produkty.query.filter_by(orderId=id).delete()
            Zamowienie.query.filter_by(id=id).delete()
            db.session.commit()
            return success_response(result, 'Order removed'), 200
        except Exception as e:
            return error_response(str(e)), 400
