from flask import render_template, redirect

# import z pliku __init__.py
from . import app, db

# import z pliku models z bieżącego katalogu
from .models import Client

# import z pliku forms z bieżącego katalogu
from .forms import ClientForm


@app.route('/')
def hello():
    # odczytanie zawartości tabeli clients
    clients = Client.query.all()

    # budujemy zmienne przekazywane do szablonu
    ctx = {'clients': clients, 'additional_param': 'Hello :-)'}

    # szablon zostanie uzupełniony zawartością zmiennych i przesłany do przeglądarki
    return render_template('clients.html', **ctx)


# przykład na obsługę metod GET i POST
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ClientForm()

    # wartość zwracana przez metodę validate_on_submit() jest True, gdy mamy do czynienia z metodą 'POST'
    if form.validate_on_submit():
        # kopiowanie przesłanych danych aby usunąć z nich pole 'csrf_token'
        validated_data = form.data.copy()
        validated_data.pop('csrf_token')

        # utworzenie obiektu typu Client (zdefiniowany w models.py)
        # dzięki zgodności nazw pól łatwiej jest zainicjalizować obiekt
        new_client = Client(**validated_data)

        # dodanie rekordu do bazy
        db.session.add(new_client)
        db.session.commit()

        # przeglądarka zostanie przekierowana na stronę główną
        return redirect('/')

    # dla metody GET protokołu HTTP zostanie zwrócony formularz z szablonu client_form.html
    return render_template('client_form.html', form=ClientForm())


# Dodatkowo: catch_all
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Próba otwarcia nietypowej ścieżki: %s' % path
