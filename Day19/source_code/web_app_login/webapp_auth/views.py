from flask.views import View

from flask import render_template, redirect, url_for, flash

# TODO: flask login import

from .models import Client

from . import app, db

from .forms import ClientForm


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


# TODO: login required
# ten widok jest dostępny tylko dla uwierzytelnionych użytkowników
@app.route('/clients/add/', methods=['GET', 'POST'])
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

# TODO: login view

#TODO: logout view

@app.route('/')
def index():
    return render_template('main_page.html')

app.add_url_rule('/clients/', view_func=ClientView.as_view('clients_list'))
