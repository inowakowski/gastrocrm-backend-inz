from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_marshmallow import Marshmallow
from credentials import *

app.config['SECRET_KEY'] = SECRET_APP_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Alergeny(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gluten = db.Column(db.Boolean, default=False) # 1 - Zboża zawierające gluten(pszenica, żyto, owies, orkisz, kamut)
    lactose = db.Column(db.Boolean, default=False) # 2 - Białka mleka krowiego
    eggs = db.Column(db.Boolean, default=False) # 3 - Jaja i produkty pochodne
    fish = db.Column(db.Boolean, default=False) # 4 - Ryby i produkty pochodne
    shellfish = db.Column(db.Boolean, default=False) # 5 - Skorupiaki
    nuts = db.Column(db.Boolean, default=False) # 6 - Orzechy(migdały, orzechy laskowe, orzechy włoskie, orzechy nerkowca, orzechy pistacjowe, orzechy brazylijskie)
    hazelnuts = db.Column(db.Boolean, default=False) # 7 - Orzechy ziemne (arachidowe)
    soya = db.Column(db.Boolean, default=False) # 8 - Soja
    sesame = db.Column(db.Boolean, default=False) # 9 - Sezam
    sulfate = db.Column(db.Boolean, default=False) # 10 - Dwutlenek siarki i siarczyny
    mustard = db.Column(db.Boolean, default=False) # 11 - Gorczyca
    lupin = db.Column(db.Boolean, default=False) # 12 - Łubin
    celery = db.Column(db.Boolean, default=False) # 13 - Seler
    molluscs = db.Column(db.Boolean, default=False) # 14 - Mięczaki

class AlergenySchema(ma.Schema):
    class Meta:
        fields = ('id', 'gluten', 'lactose', 'eggs', 'fish', 'shellfish', 'nuts', 'hazelnuts', 'soya', 'sesame', 'sulfate', 'mustard', 'lupin', 'celery', 'swordfish')
        model = Alergeny

class Czas_pracy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    waiterId = db.Column(db.Integer, db.ForeignKey('uzytkownik.id'))
    timeStart = db.Column(db.DateTime)
    timeEnd = db.Column(db.DateTime)

class Czas_pracySchema(ma.Schema):
    class Meta:
        fields = ('id', 'waiterId', 'timeStart', 'timeEnd')
        model = Czas_pracy

class Urlop_pracy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workerId = db.Column(db.Integer, db.ForeignKey('uzytkownik.id'))
    timeStart = db.Column(db.Date)
    timeEnd = db.Column(db.Date)
    status = db.Column(db.String(20))
    reason = db.Column(db.String(100))

class Urlop_pracySchema(ma.Schema):
    class Meta:
        fields = ('id', 'workerId', 'timeStart', 'timeEnd', 'status', 'reason')
        model = Urlop_pracy

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    active = db.Column(db.Boolean, default=False)
    menuFrom = db.Column(db.Date)
    menuTo = db.Column(db.Date)
    idDishDay = db.Column(db.Integer, db.ForeignKey('potrawa.id'))
    idMenuList = db.Column(db.Integer, db.ForeignKey('menu_lista.id'))

class MenuSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'active', 'menuFrom', 'menuTo', 'idDishDay', 'idMenuList')
        model = Menu

class Menu_lista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # dishNumber = db.Column(db.Integer db.ForeignKey('menu.id'))
    dishOnTheMenu = db.Column(db.String(80))

class Menu_listaSchema(ma.Schema):
    class Meta:
        fields = ('id',  'dishOnTheMenu')
        model = Menu_lista

# class Platnosc(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     zamowinieId = db.Column(db.Integer, db.ForeignKey('zamowienie.id'))
#     dataPlatnosci = db.Column(db.DateTime)
#     wartoscZamowienia = db.Column(db.Float)
#     typPlatnosciId = db.Column(db.String(80))

# class PlatnoscSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'zamowinieId', 'dataPlatnosci', 'wartoscZamowienia', 'typPlatnosciId')
#         model = Platnosc

# class Kategoria(db.Model):
#     name = db.Column(db.String(80), primary_key=True)

# class KategoriaSchema(ma.Schema):
#     class Meta:
#         model = Kategoria
#         fields = ('name',)

class Potrawa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float)
    category = db.Column(db.String(80))
    idAllergen = db.Column(db.Integer, db.ForeignKey('alergeny.id'))

class PotrawaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'category', 'idAllergen')
        model = Potrawa

class Przerwa_kelnerska(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)

class Przerwa_kelnerskaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'time')
        model = Przerwa_kelnerska

class Uzytkownik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    phoneNumber = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), nullable=False)
    tempPassword = db.Column(db.Boolean(), nullable=False, default=True)
    token = db.Column(db.String(120), unique=True)

class UzytkownikSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'firstName', 'lastName', 'phoneNumber', 'email', 'role', 'tempPassword')
        model = Uzytkownik


class Zamowienie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clientId = db.Column(db.Integer, nullable=False, autoincrement=True)
    waiterId = db.Column(db.Integer, db.ForeignKey('uzytkownik.id'))
    tableNumber = db.Column(db.Integer)
    orderDate = db.Column(db.DateTime)
    status = db.Column(db.String(80))
    summary = db.Column(db.Float)
    invoice = db.Column(db.String(12))

class ZamowienieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'clientId', 'waiterId', 'tableNumber', 'orderDate', 'status', 'invoice')
        model = Zamowienie

class Zamowienie_produkty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('zamowienie.id'))
    dishId = db.Column(db.Integer, db.ForeignKey('potrawa.id'))
    number = db.Column(db.Integer)
    price = db.Column(db.Float)

class Zamowienie_produktySchema(ma.Schema):
    class Meta:
        fields = ('id', 'orderId', 'dishId', 'number', 'price')
        model = Zamowienie_produkty

db.create_all()