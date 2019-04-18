import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('base.html', header='Hello World!')


@app.route('/clock')
def clock():
    now = datetime.datetime.now()
    # https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    datetime_format = '%Y-%m-%d %H:%M:%S'
    formatted_datetime = now.strftime(datetime_format)
    return render_template('base.html', header=formatted_datetime)


if __name__ == '__main__':
    app.run(debug=True)
