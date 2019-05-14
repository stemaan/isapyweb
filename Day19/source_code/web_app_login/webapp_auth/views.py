from flask.views import View

from flask import render_template, redirect, url_for, flash

from flask_login import current_user, login_user, logout_user, login_required

from .models import Client, User

from . import app, db

from .forms import ClientForm, LoginForm


class ListView(View):

    def get_objects(self):
        raise NotImplemented

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'clients': self.get_objects()}
        return self.render_template(context)


class ClientView(ListView):

    def get_template_name(self):
        return 'clients.html'

    def get_objects(self):
        return Client.query.all()


# ten widok jest dostępny tylko dla uwierzytelnionych użytkowników
@app.route('/clients/add/', methods=['GET', 'POST'])
@login_required
def add():
    form = ClientForm()
    if form.validate_on_submit():
        validated_data = form.data.copy()
        validated_data.pop('csrf_token')

        new_client = Client(**validated_data)
        db.session.add(new_client)
        db.session.commit()

        return redirect('/clients/')
    return render_template('client_form.html', form=ClientForm())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Jestes juz zalogowany')
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data,
                                    password=form.password.data).first()

        if user is None:
            flash('Niepoprawny login/haslo')
            return redirect(url_for('index'))

        login_user(user)
        flash('Zalogowano')
        return redirect(url_for('index'))

    return render_template('login_form.html', form=form)


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()

    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('main_page.html')


app.add_url_rule('/clients/', view_func=ClientView.as_view('clients_list'))
