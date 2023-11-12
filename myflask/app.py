from flask import Flask,render_template,request,flash,url_for,redirect

app = Flask(__name__)
app.secret_key = "!@#$%"

slist:list = [
    {
        "idno":"0001",
        "lastname":"kilo",
        "firstname":"lima",
        "course":"bsit",
        "level":"2",
    },
    {
        "idno":"0001",
        "lastname":"kilo",
        "firstname":"lima",
        "course":"bsit",
        "level":"2",
    },
    {
        "idno":"0001",
        "lastname":"kilo",
        "firstname":"lima",
        "course":"bsit",
        "level":"2",
    },
]

@app.route("/home")
def home()->None:
    return render_template("home.html", title = "home",data = slist)
    
@app.route("/login",methods=['POST','GET'])
def login()->None:
    if request.method=="POST":
        uname:str = request.form['username']
        pword:str = request.form['password']
        if uname == "admin" and pword=="user":
            return redirect(url_for("home"))
        else:
            flash("Invalid User")
            return render_template("login.html", title = "USER LOGIN")
        
    else: #Get method
        return render_template("login.html", title = "USER LOGIN")
    
#@app.route("/dashboard")
#def dashboard()->None:
#    return render_template("dashboard.html")

@app.route("/")
def main()->None:
	return "Hello World"
	
if __name__=="__main__":
	app.run(host = "0.0.0.0", debug = True)