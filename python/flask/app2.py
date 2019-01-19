from flask import Flask, render_template, request, redirect, Response
import serial

global arduino
global codes
codes = {
    "straight":b'0',
    "coast":b'1',
    "forward":b'2',
    "backward":b'3',
    "right":b'4',
    "left":b'5'
}
value = 'coast'
app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def index():
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    if request.method is 'POST':
        value = request.form['submit'].lower()
        arduino.write(codes[value])

    return render_template('index2.html', value=str(value))

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)