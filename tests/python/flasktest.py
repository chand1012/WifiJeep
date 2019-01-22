from flask import Flask, render_template, request
import serial, sys

app = Flask(__name__)
codes = {
    "straight":b'0',
    "coast":b'1',
    "forward":b'2',
    "backward":b'3',
    "right":b'4',
    "left":b'5'
}

'''
arduino = None

if sys.platform=="win32":
    arduino = serial.Serial('COM4', 9600)
else:
    arduino = serial.Serial('/dev/ttyACM0', 9600)
'''
@app.route("/")
def index():
    return render_template("index.test.html")

@app.route("/postrequest", methods = ['POST'])
def worker():
    data = request.form['byte']
    #arduino.write(codes[data])
    print("POST request recieved: sent %s" % data)
    return data

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)