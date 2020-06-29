from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Nikhil" , "Priyada" , "Mayur" , "Deepti" , "Sumant"]
    return render_template("loops.html" , names=names)
