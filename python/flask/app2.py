from flask import Flask, render_template, request, redirect, Response
import serial, sys

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

app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def index():
    arduino = None
    if sys.platform!="win32":
        arduino = serial.Serial('/dev/ttyACM0', 9600)
    else:
        try:
            for i in range(5):
                arduino = serial.Serial('COM%i' % i, 9600)
        except:
                pass

    if request.method is 'POST':
        value = request.form['submit'].lower()
        arduino.write(codes[value])
    arduino.close()
    return render_template('index2.html')

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)