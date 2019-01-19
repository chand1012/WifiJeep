from flask import Flask, render_template, request, redirect, Response
import sys, json, random
from time import time, sleep
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)
arduino.write(b'0')
app = Flask(__name__)
codes = {
    "straight":b'0',
    "coast":b'1',
    "forward":b'2',
    "backward":b'3',
    "right":b'4',
    "left":b'5'
}

@app.route("/")
def index():
    return render_template("index.html")
'''
@app.route("/postrequest", methods = ['POST'])
def worker():
    #moved forward
    data = request.get_json(force=True)
    sendbyte = None
    print(str(data))
    for thing in data:
        
        print("Sending %s" % str(thing["byte"]))
        sendbyte = str(thing["byte"]).encode()
    arduino.write(sendbyte)
'''
# this is probably overcomplicated but nothing else works
@app.route('/forward')
def forward():
    data = request.get_json(force=True)
    print(data)
    arduino.write(codes["forward"])

@app.route('/backward')
def backward():
    data = request.get_json(force=True)
    print(data)
    arduino.write(codes["backward"])

@app.route('/right')
def right():
    data = request.get_json(force=True)
    print(data)
    arduino.write(codes["right"])

@app.route('/left')
def left():
    data = request.get_json(force=True)
    print(data)
    arduino.write(codes["left"])

@app.route('/coast')
def coast():
    data = request.get_json(force=True)
    print(data)
    arduino.write(codes["coast"])

@app.route('/straight')
def straight():
    data = request.get_json(force=True)
    print(data)
    arduino.write(codes["straight"])

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)