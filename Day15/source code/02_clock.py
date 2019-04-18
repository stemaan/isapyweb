import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/')
def clock():
    # odczytujemy aktualny czas
    now = datetime.datetime.now()
    
    # zamieniamy obiekt datetime na stringa wg zdefiniowanego wzorca
    # https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior
    datetime_format = '%Y-%m-%d %H:%M:%S'
    return now.strftime(datetime_format)


if __name__ == '__main__':
    app.run(debug=True)
