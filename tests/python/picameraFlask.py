import io
import sys
from threading import Condition

import serial
from flask import Flask, Response, jsonify, render_template, request

import picamera

cam = picamera.PiCamera(resolution='640x480', framerate=24)
app = Flask(__name__)

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

@app.route("/")
def index():
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')
    return render_template("index.test.html")

@app.route("/postrequest", methods = ['POST'])
def worker():
    data = request.form['byte']
    print("POST request recieved: sent %s" % data)
    return data

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)