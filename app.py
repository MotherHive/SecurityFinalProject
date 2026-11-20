from flask import Flask, request, redirect, url_for, render_template
from models.users import User

from extensions import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SECRET_KEY'] = os.getenv("DATABASE_KEY")

db.init_app(app)

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