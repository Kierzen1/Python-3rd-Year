from flask import Flask,render_template,request,flash,url_for

app = Flask(__name__)

@app.route("/login",methods=['POST','GET'])
def userLogin()->None:
    if request.method=="POST":
        #Get the inputted Value
        uname:str = request.form['username']
        pword:str = request.form['password']
        if uname == "admin" and pword=="user":
            return url_for("main")
        else:
            flash("Invalid User")
            return render_template("login.html")
        
    else: #Get method
        return render_template("login.html")
    
#@app.route("/dashboard")
#def dashboard()->None:
#    return render_template("dashboard.html")

@app.route("/")
def main()->None:
	return "Hello World"
	
if __name__=="__main__":
	app.run()