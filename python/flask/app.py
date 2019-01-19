from flask import Flask, render_template, request, redirect, Response
import sys, json
import serial

app = Flask(__name__)
codes = {
    "straight":b'0',
    "coast":b'1',
    "forward":b'2',
    "backward":b'3',
    "right":b'4',
    "left":b'5'
}

@app.route("/", methods = ['POST', 'GET'])
def index():
    global arduino 
    if sys.platform!="win32":
        arduino = serial.Serial('/dev/ttyACM0', 9600)
    else:
        for i in range(5):
            try:
                arduino = serial.Serial('COM%i' % i, 9600)
            except:
                pass
    data = request.get_json()
    sendbyte = None
    print(str(data))
    if request.method == 'POST':
        for thing in data:
            if type(thing["byte"]) is int:
                print("Sending %s" % str(thing["byte"]))
                sendbyte = str(thing["byte"]).encode()
        arduino.write(sendbyte)

    return render_template("index.html")

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)