from unittest import result
from flask import request, Flask
import uuid
from utils.uitils import *
import random, string, secrets
from db.db_config import *

dish_schema = PotrawaSchema()
dishes_schema = PotrawaSchema(many=True)
allergen_schema = AlergenySchema()
allergens_schema = AlergenySchema(many=True)

# Pobierz potrawy.
def get_dishes():
    if request.method == 'GET':
        try:
            dish = Potrawa.query.all()
            result = dishes_schema.dump(dish)
            return success_response(result, 'Pobrano potrawy'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Pobierz potrawy.
def get_dish(id):
    if request.method == 'GET':
        try:
            dish = Potrawa.query.filter_by(id=id).first()
            allergen = Alergeny.query.filter_by(id=dish.idAllergen).first()
            result = {
                'id': dish.id,
                'name': dish.name,
                'price': dish.price,
                'category': dish.category,
                'allergen': {
                    'id': allergen.id,
                    'gluten': allergen.gluten,
                    'lactose': allergen.lactose,
                    'eggs': allergen.eggs,
                    'fish': allergen.fish,
                    'shellfish': allergen.shellfish,
                    'nuts': allergen.nuts,
                    'hazelnuts': allergen.hazelnuts,
                    'soya': allergen.soya,
                    'sesame': allergen.sesame,
                    'sulfate': allergen.sulfate,
                    'mustard': allergen.mustard,
                    'lupin': allergen.lupin,
                    'celery': allergen.celery,
                    'molluscs': allergen.molluscs
                }
            }
            return success_response(result, 'Pobrano potrawę'), 200
        except Exception as e:
            return error_response(str(e)), 400

def get_allergen(id):
    if request.method == 'GET':
        try:
            allergen = Alergeny.query.filter_by(id=id).first()
            result = allergen_schema.dump(allergen)
            return success_response(result, 'Pobrano alergen'), 200
        except Exception as e:
            return error_response(str(e)), 400

def get_allergens():
    if request.method == 'GET':
        try:
            allergen = Alergeny.query.all()
            result = allergens_schema.dump(allergen)
            return success_response(result, 'Pobrano alergeny'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Dodaj potrawę.
def add_dish_api():
    if request.method == 'PUT':
        try:
            data = request.get_json()
            allergen_in_dish = Alergeny()
            if 'gluten' in data:
                allergen_in_dish.gluten = data['gluten']
            if 'lactose' in data:
                allergen_in_dish.lactose = data['lactose']
            if 'eggs' in data:
                allergen_in_dish.eggs = data['eggs']
            if 'fish' in data:
                allergen_in_dish.fish = data['fish']
            if 'shellfish' in data:
                allergen_in_dish.shellfish = data['shellfish']
            if 'nuts' in data:
                allergen_in_dish.nuts = data['nuts']
            if 'hazelnuts' in data:
                allergen_in_dish.hazelnuts = data['hazelnuts']
            if 'soya' in data:
                allergen_in_dish.soya = data['soya']
            if 'sesame' in data:
                allergen_in_dish.sesame = data['sesame']
            if 'sulfate' in data:
                allergen_in_dish.sulfate = data['sulfate']
            if 'mustard' in data:
                allergen_in_dish.mustard = data['mustard']
            if 'lupin' in data:
                allergen_in_dish.lupin = data['lupin']
            if 'celery' in data:
                allergen_in_dish.celery = data['celery']
            if 'molluscs' in data:
                allergen_in_dish.molluscs = data['molluscs']
            db.session.add(allergen_in_dish)
            db.session.commit()
            allergen = Alergeny.query.order_by(Alergeny.id.desc()).first()
            dish = Potrawa()
            if 'name' in data:
                dish.name = data['name']
            if 'price' in data:
                dish.price = data['price']
            if 'category' in data:
                dish.category = data['category']
            dish.idAllergen = allergen.id
            db.session.add(dish)
            db.session.commit()
            result = {
                'id': dish.id,
                'name': dish.name,
                'price': dish.price,
                'category': dish.category,
                'allergen': {
                    'id': allergen.id,
                    'gluten': allergen.gluten,
                    'lactose': allergen.lactose,
                    'eggs': allergen.eggs,
                    'fish': allergen.fish,
                    'shellfish': allergen.shellfish,
                    'nuts': allergen.nuts,
                    'hazelnuts': allergen.hazelnuts,
                    'soya': allergen.soya,
                    'sesame': allergen.sesame,
                    'sulfate': allergen.sulfate,
                    'mustard': allergen.mustard,
                    'lupin': allergen.lupin,
                    'celery': allergen.celery,
                    'molluscs': allergen.molluscs
                }
            }
            return success_response(result,'Dodano potrawę'), 201
        except Exception as e:
            return error_response(str(e), data), 400

# Dodaj kategorię.
# def category_api(id=None):
#     if request.method == 'GET':
#         try:
#             category = Kategoria.query.all()
#             result = categories_schema.dump(category)
#             return success_response(result, 'Pobrano kategorie')
#         except Exception as e:
#             return error_response(str(e))
#     if request.method == 'PUT':
#         try:
#             data = request.get_json()
#             category = Kategoria(name=data['name'])
#             db.session.add(category)
#             db.session.commit()
#             return success_message('Dodano kategorię')
#         except Exception as e:
#             return error_response(str(e))
#     if request.method == 'DELETE':
#         try:
#             Kategoria.query.filter_by(name=id).delete()
#             db.session.commit()
#             return success_message('Usunięto kategorię')
#         except Exception as e:
#             return error_response(str(e))

# Edytuj potrawę.
def edit_dish_api(id):
    if request.method == 'PATCH':
        try:
            data = request.get_json()
            dish = Potrawa.query.filter_by(id=id).first()
            allergen = Alergeny.query.filter_by(id=dish.idAllergen).first()
            if 'name' in data:
                dish.name = data['name']
            if 'price' in data:
                dish.price = data['price']
            if 'category' in data:
                dish.category = data['category']
            if 'gluten' in data:
                allergen.gluten = data['gluten']
            if 'lactose' in data:
                allergen.lactose = data['lactose']
            if 'eggs' in data:
                allergen.eggs = data['eggs']
            if 'fish' in data:
                allergen.fish = data['fish']
            if 'shellfish' in data:
                allergen.shellfish = data['shellfish']
            if 'nuts' in data:
                allergen.nuts = data['nuts']
            if 'hazelnuts' in data:
                allergen.hazelnuts = data['hazelnuts']
            if 'soya' in data:
                allergen.soya = data['soya']
            if 'sesame' in data:
                allergen.sesame = data['sesame']
            if 'sulfate' in data:
                allergen.sulfate = data['sulfate']
            if 'mustard' in data:
                allergen.mustard = data['mustard']
            if 'lupin' in data:
                allergen.lupin = data['lupin']
            if 'celery' in data:
                allergen.celery = data['celery']
            if 'molluscs' in data:
                allergen.molluscs = data['molluscs']                
            db.session.commit()
            result = {
                'id': dish.id,
                'name': dish.name,
                'price': dish.price,
                'category': dish.category,
                'allergen': {
                    'id': allergen.id,
                    'gluten': allergen.gluten,
                    'lactose': allergen.lactose,
                    'eggs': allergen.eggs,
                    'fish': allergen.fish,
                    'shellfish': allergen.shellfish,
                    'nuts': allergen.nuts,
                    'hazelnuts': allergen.hazelnuts,
                    'soya': allergen.soya,
                    'sesame': allergen.sesame,
                    'sulfate': allergen.sulfate,
                    'mustard': allergen.mustard,
                    'lupin': allergen.lupin,
                    'celery': allergen.celery,
                    'molluscs': allergen.molluscs
                }
            }
            return success_response(result,'Zmieniono potrawę'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Usuń potrawę.
def delete_dish_api(id):
    if request.method == 'DELETE':
        try:
            dish = Potrawa.query.filter_by(id=id).first()
            allergen = Alergeny.query.filter_by(id=dish.idAllergen).first()
            result = {
                'id': dish.id,
                'name': dish.name,
                'price': dish.price,
                'category': dish.category,
                'allergen': {
                    'id': allergen.id,
                    'gluten': allergen.gluten,
                    'lactose': allergen.lactose,
                    'eggs': allergen.eggs,
                    'fish': allergen.fish,
                    'shellfish': allergen.shellfish,
                    'nuts': allergen.nuts,
                    'hazelnuts': allergen.hazelnuts,
                    'soya': allergen.soya,
                    'sesame': allergen.sesame,
                    'sulfate': allergen.sulfate,
                    'mustard': allergen.mustard,
                    'lupin': allergen.lupin,
                    'celery': allergen.celery,
                    'molluscs': allergen.molluscs
                }
            }
            db.session.delete(dish)
            db.session.commit()
            db.session.delete(allergen)
            db.session.commit()
            return success_response(result, 'Usunięto potrawę'), 200
        except Exception as e:
            return error_response(str(e)), 400

# Usuń kategorię.

