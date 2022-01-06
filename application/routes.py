from application import app
from flask import render_template


@app.route("/")#decorator
def home():
    return render_template("index.html")


@app.route("/login")
def login_():
    return render_template('/includes/login.html')


@app.route("/check-your-health-advanced")
def check_your_health_advanced():
    return render_template('/includes/check_your_health_advanced.html')