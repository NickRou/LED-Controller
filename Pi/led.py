from flask import Flask, render_template, redirect, url_for, request
from Pi.led_controls import LED

"""
sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python led.py
"""
app = Flask(__name__)
led = LED()

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == "POST":
        userInput = request.form.get('userInput')
        if userInput == 'rainbow':
            led.rainbow()
        elif userInput == 'rainbow cycle':
            led.rainbowCycle()
        else: 
            led.colorWipe(userInput)
        
    return render_template('main.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
