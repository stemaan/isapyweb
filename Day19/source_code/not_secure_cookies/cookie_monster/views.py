from flask import render_template, redirect, url_for, make_response, request

from . import app
from .forms import CookieForm


# strona główna przekierowuje na formularz ciasteczkowy
@app.route('/')
def hello():
    return redirect(url_for('add'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CookieForm()

    if form.validate_on_submit():
        validated_data = form.data.copy()
        validated_data.pop('csrf_token')

        # tworzę odpowiedź, która będzie przekierowywała na formularz
        response = make_response(redirect(url_for('add')))
        # w odpowiedzi ustawiam otrzymane cookie
        response.set_cookie(validated_data['cookie_name'], validated_data['cookie_value'])
        # zwracam odpowiedź
        return response

    # tutaj zostanie uzupełniony i zwrócony szablon. Uzupełniam o formularz i zawartość ciasteczek przeglądarki
    return render_template('cookies.html', form=CookieForm(), cookies=request.cookies)


@app.route('/delete')
def delete():
    cookie_id = request.args.get('id')

    response = make_response(redirect(url_for('add')))
    response.delete_cookie(cookie_id)

    return response
