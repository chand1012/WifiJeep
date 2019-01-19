from flask import Flask, render_template, request, redirect, Response
import sys, json, random
from time import time, sleep
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
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    data = request.get_json(force=True)
    sendbyte = None
    print(str(data))
    for thing in data:
        if type(thing["byte"]) is int:
            print("Sending %s" % str(thing["byte"]))
            sendbyte = str(thing["byte"]).encode()
    arduino.write(sendbyte)

    return render_template("index.html")

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)