from flask import Flask

#app is a variable
app = Flask(__name__)

@app.route("/")
def index():
    return " (Marathi) Namaskar Mandali... "+" (मराठी) _^_ नमस्कार मंडळी "+" (German) Hallo Leute!! "+" (English) Hello People!! "


@app.route("/aditi")
def aditi():
    return "Hello, Aditi! You Have Done It!! Gr8! refresh is working using export FLASK_DEBUG=1"

@app.route("/angad")
def angad():
    return "Namaskar Angad _^_ !! :) "

@app.route("/<string:name>")
def namaskar(name):
    return f"Namaskar, {name} _^_ !"
