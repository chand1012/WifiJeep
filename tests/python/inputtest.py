from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.test.html")

@app.route("/postrequest", methods = ['POST'])
def worker():
    data = request.form['byte']
    print("POST request recieved: sent %s" % data)
    return data

if __name__=="__main__":
    app.run('0.0.0.0', "1166", debug=True)