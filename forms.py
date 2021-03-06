from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_form.html")

#If we directly on webpage url hit the url with /hello it gives following error
#Method Not Allowed
#The method is not allowed for the requested URL.
#bcoz here we defined methods POST and when we hit url directly it is GET methods
#so it's a mismatch that's why not allowed
#solution methods=["GET" , "POST"] output : Hello , None without if else conditions
@app.route("/hello" , methods=["GET" , "POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead.."
    else:
        name = request.form.get("name")
        return render_template("hello.html" , name=name)
