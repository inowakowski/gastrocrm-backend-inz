from flask import request
from utils.uitils import *
from db.db_config import *

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)
menuLista_schema = Menu_listaSchema()
menuListy_schema = Menu_listaSchema(many=True)

#Menu.
def menu_api(id=None):
    if request.method == 'GET':
# Get all menus.
        if id is None:
            menu = Menu.query.all()
            result = menus_schema.dump(menu)
            return success_response(result, 'Pobrano wszystkie menu')
# Get one menu.
        else:
            menu = Menu.query.filter_by(id=id).first()
            menu_lista = Menu_lista.query.filter_by(id=menu.idMenuList).first()
            menu = menu_schema.dump(menu)
            dishOnTheMenu = menu_lista.dishOnTheMenu.strip('[]').split(',')
            for i in range(len(dishOnTheMenu)):
                dishOnTheMenu[i] = int(dishOnTheMenu[i])
            result = {
                "menu": menu,
                "dishOnTheMenu": dishOnTheMenu
            }
            return success_response(result, 'Menu'), 200
# Add new menu.
    if request.method == 'PUT':
        try:
            data = request.get_json()
            menu_lista = Menu_lista()
            menu_lista.dishOnTheMenu = str(data['dishOnTheMenu'])
            db.session.add(menu_lista)
            db.session.commit()
            menu_lista = Menu_lista.query.order_by(Menu_lista.id.desc()).first()
            menu = Menu()
            if 'title' in data:
                menu.title = data['title']
            if 'active' in data:
                menu.active = data['active']
            if 'menuFrom' in data:
                menu.menuFrom = data['menuFrom']
            if 'menuTo' in data:
                menu.menuTo = data['menuTo']
            if 'idDishDay' in data:
                menu.idDishDay = data['idDishDay']
            menu.idMenuList = menu_lista.id
            db.session.add(menu)
            db.session.commit()
            menu = Menu.query.order_by(Menu.id.desc()).first()
            result = menu_schema.dump(menu)
            return success_response(result, 'Dodano menu'), 201
        except Exception as e:
            return error_response(str(e)), 400
# Edit menu.
    if request.method == 'PATCH':
        try:
            data = request.get_json()
            menu = Menu.query.filter_by(id=id).first()
            result = menu_schema.dump(menu)
            if len(result) == 0:
                return error_response('Nie znaleziono menu'), 404
            else:
                if 'title' in data:
                    menu.title = data['title']
                if 'active' in data:
                    menu.active = data['active']
                if 'menuFrom' in data:
                    menu.menuFrom = data['menuFrom']
                if 'menuTo' in data:
                    menu.menuTo = data['menuTo']
                if 'idDishDay' in data:
                    menu.idDishDay = data['idDishDay']
                if 'dishOnTheMenu' in data:
                    menu_lista = Menu_lista.query.filter_by(id=menu.idMenuList).first()
                    menu_lista.dishOnTheMenu = str(data['dishOnTheMenu'])
                db.session.commit()
            menu = Menu.query.filter_by(id=id).first()
            result = {
                "menu": menu_schema.dump(menu),
                "dishOnTheMenu": menu_lista.dishOnTheMenu.strip('[]').split(',')
            }
            return success_response(result, 'Edytowano menu'), 200
        except Exception as e:
            return error_response(str(e)), 400
# Delete menu.
    if request.method == 'DELETE':
        try:
            menu = Menu.query.filter_by(id=id).first()
            menu_lista = Menu_lista.query.filter_by(id=menu.idMenuList).first()
            result = {
                "menu": menu_schema.dump(menu),
                "dishOnTheMenu": menu_lista.dishOnTheMenu.strip('[]').split(',')
            }
            db.session.delete(menu_lista)
            db.session.delete(menu)
            db.session.commit()
            return success_response(result,'Usunięto menu'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Lista menu.
def menu_list_api(id=None):
# Get all menu lists.
    if request.method == 'GET':
        try:
            if id:
                menu_lista = Menu_lista.query.filter_by(id=id).all()
            else:
                menu_lista = Menu_lista.query.all()
            for i in range(len(menu_lista)):
                dishOnTheMenu = menu_lista[i].dishOnTheMenu.strip('[]').split(',')
                for j in range(len(dishOnTheMenu)):
                    dishOnTheMenu[j] = int(dishOnTheMenu[j])
                menu_lista[i].dishOnTheMenu = dishOnTheMenu
            result = menuListy_schema.dump(menu_lista)
            return success_response(result, 'Lista menu'), 200
        except Exception as e:
            return error_response(str(e)), 400
# Delete menu list.
    if request.method == 'DELETE':
        try:
            menu_lista = Menu_lista.query.filter_by(id=id).first()
            db.session.delete(menu_lista)
            db.session.commit()
            return success_response(menu_lista, 'Usunięto listę menu'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Wyświetl aktualne menu.
def get_active_menu_api():
    if request.method == 'GET':
        try:
            menu = Menu.query.filter_by(active=True).all()
            result = menus_schema.dump(menu)
            return success_response(result, 'Aktywne menu'), 200
        except Exception as e:
            return error_response(str(e)), 400


# def add_dish_to_menu_api(id):
#     if request.method == 'PUT':
#         try:
#             data = request.get_json()

#             menu_lista = Menu_lista.query.order_by(Menu_lista.id.desc()).first()
#             menu = Menu.query.filter_by(id=id).first()
#             menu.idMenuList = menu_lista.id
#             db.session.commit()
#             return success_response(menu_lista, 'Dodano potrawę do menu')
#         except Exception as e:
#             return error_response(str(e))


# def delete_dish_from_menu_api(id):
#     if request.method == 'DELETE':
#         try:
#             menu_lista = Menu_lista.query.filter_by(id=id).first()
#             db.session.delete(menu_lista)
#             db.session.commit()
#             return success_response(menu_lista, 'Usunięto potrawę z menu')
#         except Exception as e:
#             return error_response(str(e))
