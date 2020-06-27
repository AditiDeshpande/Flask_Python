from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Aditi.. You Have Done It!! Gr8! refresh is working using export FLASK_DEBUG=1"
