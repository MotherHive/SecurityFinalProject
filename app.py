from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

test_user_database = {"admin": "password"}

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username_input = request.form.get("username")
        password_input = request.form.get("password")
        
        password = test_user_database.get(username_input, None)
        
        if password and password == password_input:
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")
    
    return render_template("login.html")

if __name__ == 'main':
    app.run(debug=True)