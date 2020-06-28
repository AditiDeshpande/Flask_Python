from flask import Flask

#app is a variable
app = Flask(__name__)

@app.route("/")
def index():
    return "Namaskar Mandali...!!"

@app.route("/aditi")
def aditi():
    return "Hello, Aditi! You Have Done It!! Gr8! refresh is working using export FLASK_DEBUG=1"
