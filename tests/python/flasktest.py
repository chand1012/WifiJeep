from flask import Flask, render_template, request, Response, jsonify
import serial, sys
from webcamera import VideoCamera

app = Flask(__name__)


def video_stream(): # this is the issue
    global video_camera
    global global_frame
    video_camera = None
    global_frame = None
    if video_camera == None:
        video_camera = VideoCamera()
    
    while True:
        frame = video_camera.get_frame()

        if frame != None:
            global_frame = frame
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')


@app.route("/")
def index():
    return render_template("index.test.html")

@app.route("/postrequest", methods = ['POST'])
def worker():
    data = request.form['byte']
    print("POST request recieved: sent %s" % data)
    return data

@app.route("/record_status", methods=['POST'])
def record_status():
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera()

    json = request.get_json()

    status = json['status']

    if status == "true":
        video_camera.start_record()
        return jsonify(result="started")
    else:
        video_camera.stop_record()
        return jsonify(result="stopped")

@app.route("/record")
def video_viewer():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)