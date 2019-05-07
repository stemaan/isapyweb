from flask.views import View
from flask import render_template

from .models import Client
from . import app


class ListView(View):
    template_name = 'objects_list.html'

    def get_objects(self):
        raise NotImplementedError()

    def get_context(self):
        return {'objects': self.get_objects()}

    def render_template(self, context):
        return render_template(self.__class__.template_name, **context)

    def dispatch_request(self):
        return self.render_template(self.get_context())


class ClientListView(ListView):
    template_name = 'client_list.html'

    def get_objects(self):
        return Client.query.all()


app.add_url_rule('/clients', view_func=ClientListView.as_view('client_list'))
