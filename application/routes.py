from application import app
from flask import render_template


@app.route("/")#decorator
def home():
    return render_template("index.html")


@app.route("/login")
def login_():
    return render_template('/includes/login.html')


@app.route("/check_your_health")
def check_your_health():
    return render_template('/includes/check_your_health.html')