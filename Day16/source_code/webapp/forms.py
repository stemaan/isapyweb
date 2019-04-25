from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, DataRequired


class ClientForm(FlaskForm):
    first_name = StringField('Imie', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Nazwisko', validators=[DataRequired(), Length(min=2, max=64)])
    password = PasswordField('Hasło', validators=[DataRequired()])
