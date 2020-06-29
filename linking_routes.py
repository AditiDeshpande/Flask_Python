from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index_for_linking():
    return render_template("index_for_linking.html")

@app.route("/more")
def more():
    return render_template("more.html")
