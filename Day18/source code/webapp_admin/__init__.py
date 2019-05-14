from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'infosharepythonsredniozaawansowany2019'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# mamy możliwość ustawienia tematu dla panelu
# nazwy tematów dostępne są na stronie: https://bootswatch.com/3/
app.config['FLASK_ADMIN_SWATCH'] = 'paper'

db = SQLAlchemy(app)

# utworzenie obiektu klasy Flask-Admin i przypięcie go do aplikacji
admin = Admin(app, name='Przeglądarka kont i adresów', template_mode='bootstrap3')

from . import models

db.create_all()

# Wskazujemy, które modele (models.Client, model.Address) będą zarządzane przez panel administracyjny 
admin.add_view(ModelView(models.Client, db.session))
admin.add_view(ModelView(models.Address, db.session))

from . import views
from . import forms

