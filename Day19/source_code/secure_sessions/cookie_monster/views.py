from flask import session, render_template, redirect, url_for, request

from . import app
from .forms import CookieForm


@app.route('/')
def hello():
    return redirect(url_for('add'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CookieForm()

    if form.validate_on_submit():
        validated_data = form.data.copy()
        validated_data.pop('csrf_token')

        # w sesji ustawiam przekazany wpis
        session[validated_data['cookie_name']] =  validated_data['cookie_value']
        return redirect(url_for('add'))

    return render_template('cookies.html', form=CookieForm(), cookies=session)


@app.route('/delete')
def delete():
    cookie_id = request.args.get('id')
    session.pop(cookie_id)
    return redirect(url_for('add'))
