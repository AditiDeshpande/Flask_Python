from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello You!!"
    return render_template("index.html" , headline=headline)

@app.route("/bye")
def bye():
    headline = "Auf Wiedersehen"
    return render_template("index.html" , headline=headline)
