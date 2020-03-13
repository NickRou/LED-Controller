from flask import Flask, render_template, redirect, url_for, request
from flask_jsglue import JSGlue
from Pi.led_controls import LED

"""
sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python led.py
"""
app = Flask(__name__)
jsglue = JSGlue(app)
led = LED()

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == "POST":
        rgbString = request.form.get('rgbString')
        try:
            print("Color change to {}".format(rgbString))
            led.colorWipe(rgbString)
        except TypeError: 
            print("Type Error")
        
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
