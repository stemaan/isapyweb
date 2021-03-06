from flask.views import View
from flask import render_template, redirect

from .models import Client, Address
from . import app, db
from .forms import ClientForm, AddressForm


@app.route('/')
def index():
    return render_template('main_page.html')


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


@app.route('/addresses/add/', methods=['GET', 'POST'])
def add_address():
    form = AddressForm()
    if form.validate_on_submit():
        validated_data = form.data.copy()
        validated_data.pop('csrf_token')

        new_client = Address(**validated_data)
        db.session.add(new_client)
        db.session.commit()

        return redirect('/addresses/')
    return render_template('address_form.html', form=AddressForm())


class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)


class ClientView(ListView):

    def get_template_name(self):
        return 'clients.html'

    def get_objects(self):
        return Client.query.all()


class AddressListtView(ListView):

    def get_template_name(self):
        return 'adresses.html'

    def get_objects(self):
        return Address.query.all()


app.add_url_rule('/clients/', view_func=ClientView.as_view('clients_list'))
app.add_url_rule('/addresses/', view_func=AddressListtView.as_view('addresses_list'))
