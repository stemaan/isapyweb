
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):
    first_name = StringField('imie', validators=[DataRequired()])
    last_name = StringField('nazwisko', validators=[DataRequired()])


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
