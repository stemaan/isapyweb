
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'infosharepythonsredniozaawansowany2019'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from . import views
from . import forms

