from flask import Flask, render_template, redirect, url_for, request
from Pi.led_controls import LED
import re

"""
sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/strandtest.py
"""
app = Flask(__name__)
led = LED()

@app.route("/")
def root():
    templateData = {
        'title' : 'Pi',
    }

    return render_template('main.html', **templateData)


@app.route("/color", methods=['GET', 'POST'])
def color():
    if request.method == 'POST':
        print(request.form['color'])
        led.colorWipe(request.form['color'])
        return render_template('main.html')
    return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
