
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):
    first_name = StringField('imie', validators=[DataRequired()])
    last_name = StringField('nazwisko', validators=[DataRequired()])


# TODO: login form
