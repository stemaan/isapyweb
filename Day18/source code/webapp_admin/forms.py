from flask_wtf import FlaskForm
from wtforms_alchemy import ModelForm
from wtforms import StringField
from wtforms.validators import DataRequired

from .models import Address


class ClientForm(FlaskForm):
    first_name = StringField('imie', validators=[DataRequired()])
    last_name = StringField('nazwisko', validators=[DataRequired()])


class AddressForm(ModelForm, FlaskForm):
    class Meta:
        model = Address
