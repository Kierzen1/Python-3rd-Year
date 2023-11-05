from flask import Flask,request,render_template 

app = Flask(__name__)

@app.route("/login")
def Login()->None:
    return render_template("login.html")
    
@app.route("/") 
def main()->None:
    return "Hello World"
    
if __name__ == "__main__":
    app.run(debug =True)