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

def arduinowrite():
    arduino = serial.Serial('COM4', 9600)
    arduino.write()


@app.route("/", methods = ['POST', 'GET'])
def index():
    
    return render_template("index.html")

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)