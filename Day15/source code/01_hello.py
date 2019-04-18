from flask import Flask

# tworzymy obiekt aplikacji
app = Flask(__name__)


# żądania '/' będą obsługiwane przez funkcję hello()
@app.route('/')
def hello():
    # treść zwracana do przeglądarki
    return 'Hello World!'


# aplikacja uruchomi się tylko przy bezpośrednim wywołaniu (nie uruchomi się gdy kod będzie importowany)
if __name__ == '__main__':

    # bardzo przydatne ustawienie (eliminuje restart aplikacji). Nie używaj na produkcji!
    app.run(debug=True)
