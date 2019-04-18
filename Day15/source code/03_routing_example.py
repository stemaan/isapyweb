import datetime
from flask import Flask

app = Flask(__name__)


# w jednym pliku można obsługiwać różne żądania 
@app.route('/clock')
def clock():
    now = datetime.datetime.now()
    # https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    datetime_format = '%Y-%m-%d %H:%M:%S'
    return now.strftime(datetime_format)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
