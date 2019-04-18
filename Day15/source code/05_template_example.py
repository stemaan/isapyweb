import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def clock():
    now = datetime.datetime.now()
    # https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    datetime_format = '%Y-%m-%d %H:%M:%S'
    formatted_datetime = now.strftime(datetime_format)
    template_name = 'clock.html'

    # zwracamy szablon `template_name` wypełniony na podstawie przekazanego obiektu `current_date_and_time`
    return render_template(template_name, current_date_and_time=formatted_datetime)


if __name__ == '__main__':
    app.run(debug=True)
