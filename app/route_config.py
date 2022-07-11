import time
from flask import Flask
from api.api_user import *
from api.api_dish import *
from api.api_menu import *
from api.api_order import *
from api.api_worktime import *
from api.api_statistic import *
from app import app
from utils.uitils import *
from db.db_config import *

@app.route('/api/get-<domain>', methods=['GET', 'POST'])
@auth_required
def get(domain):
    if domain == 'dishes':
        return get_dishes()
    elif domain == 'users':
        return get_users()
    elif domain == 'orders':
        return get_orders_api()
    elif domain == 'active-menu':
        return get_active_menu_api()
    elif domain == 'all-menu':
        return menu_api()
    elif domain == 'menu-list':
        return menu_list_api()
    elif domain == 'allergens':
        return get_allergens()
    elif domain == 'break-time':
        return breaktime_api()
    elif domain == 'holidays':
        return holiday_api()
    elif domain == 'worktime-statistics':
        return show_statistics_time()
    elif domain == 'sales-statistics':
        return show_statistics_sales()
    else:
        return "error request probable not exist", 400

@app.route('/api/get-<domain>/<id>', methods=['GET', 'POST'])
@auth_required
def get_with_id(domain, id):
    if domain == 'dish':
        return get_dish(id)
    elif domain == 'menu':
        return menu_api(id)
    elif domain == 'user':
        return get_user(id)
    elif domain == 'allergen':
        return get_allergen(id)
    elif domain == 'summary-order':
        return summary_order_api(id)
    elif domain == 'working-time':
        return worktime_api(id)
    elif domain == 'holiday':
        return holiday_api(id)
    elif domain == 'orders':
        return get_orders_api(id)
    elif domain == 'order':
        return get_order_api(id)
    elif domain == 'users-by-role':
        return get_users_by_role(id)
    elif domain == 'waiter-sales-statistics':
        return show_waiter_sale_statistics(id)
    elif domain == 'worktime-statistics':
        return show_statistics_time(id)
    elif domain == 'invoice':
        return invoice_order_api(id)
    else:
        return "error request probable not exist", 400

@app.route('/api/add-<domain>', methods=['PUT'])
@auth_required
def add(domain):
    if domain == 'dish':
        return add_dish_api()
    elif domain == 'menu':
        return menu_api()
    elif domain == 'user':
        return add_user_api()
    elif domain == 'working-time':
        return worktime_api()
    elif domain == 'break-time':
        return breaktime_api()
    elif domain == 'holiday':
        return holiday_api()
    elif domain == 'order':
        return add_dish_to_order_api()
    else:
        return "error request probable not exist", 400


@app.route('/api/edit-<domain>/<id>', methods=['PATCH'])
@auth_required
def edit_with_id(domain, id):
    if domain == 'dish':
        return edit_dish_api(id)
    elif domain == 'menu':
        return menu_api(id)
    elif domain == 'user':
        return edit_user_api(id)
    elif domain == 'break-time':
        return breaktime_api(id)
    elif domain == 'order':
        return edit_order_api(id)
    elif domain == 'working-time':
        return worktime_api(id)
    elif domain == 'holiday':
        return holiday_api(id)
    else:
        return "error request probable not exist", 400

@app.route('/api/edit-<domain>', methods=['PATCH'])
@auth_required
def edit(domain):
    if domain == 'break-time':
        return breaktime_api()
    else:
        return "error", 400

@app.route('/api/pay-order/<id>', methods=['PATCH'])
@auth_required
def pay_order(id):
    return pay_order_api(id)

@app.route('/api/summary-order/<id>', methods=['PATCH'])
@auth_required
def summary_order(id):
    return summary_order_api(id)

@app.route('/api/add-invoice/<id>', methods=['PATCH'])
@auth_required
def add_invoice(id):
    return invoice_order_api(id)

@app.route('/api/delete-<domain>/<id>', methods=['DELETE'])
@auth_required
def delete(domain, id):
    if domain == 'dish':
        return delete_dish_api(id)
    elif domain == 'menu':
        return menu_api(id)
    elif domain == 'user':
        return delete_user_api(id)
    elif domain == 'break-time':
        return breaktime_api(id)
    elif domain == 'holiday':
        return holiday_api(id)
    elif domain == 'working-time':
        return worktime_api(id)
    elif domain == 'order':
        return delete_order_api(id)
    else:
        return "error request probable not exist", 400

@app.route('/api/login', methods=['GET', 'POST'])
def login_user():
    return login()

@app.route('/api/active-user/<username>', methods=['PATCH'])
def active_user(username):
    return active_user_api(username)

@app.route('/api/forgot-password', methods=['GET', 'POST'])
def forgot_passwd():
    return forgot_password()

@app.route('/api/change-password/<nazwaUzytkownika>', methods=['PATCH'])
def change_passwd(nazwaUzytkownika):
    return change_password(nazwaUzytkownika)

@app.route('/api/create-account', methods=['PUT'])
def create_account():
    return add_user_api()

@app.after_request
def after_request(response):
    return response

@app.route('/api/health', methods=['GET'])
def health_check():
    return "OK"

@app.route('/api/add-unavailability', methods=['POST'])
@auth_required
def add_unavailability():
    return add_unavailability_api()

