
from flask_wtf import FlaskForm
from wtforms import StringField

from wtforms.validators import DataRequired

class CookieForm(FlaskForm):

    cookie_name = StringField('Nazwa cookie', validators=[DataRequired()])
    cookie_value = StringField('Wartość cookie', validators=[DataRequired()])
