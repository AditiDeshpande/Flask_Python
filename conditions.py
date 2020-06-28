import datetime

from flask import Flask  , render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    #new_year is boolean
    #new_year = True
    # Above line is to force to show happy new year :)
    return render_template("isItNewYear.html" , new_year=new_year)
