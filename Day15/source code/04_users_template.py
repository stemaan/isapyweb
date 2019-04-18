from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    users = list()
    user = {'username': 'Mickey Mouse', 'url': 'https://en.wikipedia.org/wiki/Mickey_Mouse'}
    users.append(user)
    user = {'username': 'Donald Duck', 'url': 'https://en.wikipedia.org/wiki/Donald_Duck'}
    users.append(user)
    user = {'username': 'Goofy', 'url': 'https://en.wikipedia.org/wiki/Goofy'}
    users.append(user)
    user = {'username': 'Pluto', 'url': 'https://en.wikipedia.org/wiki/Pluto_(Disney)'}
    users.append(user)

    # zwracamy szablon `template_name` wypełniony na podstawie przekazanego obiektu `users`
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
