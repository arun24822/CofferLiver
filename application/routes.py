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


@app.route("/check-your-health-common")
def check_your_health_common():
    return render_template('/includes/check-your-health-common.html')


# class User(db.Document):
#     user_id     =   db.IntField(unique=True)
#     first_name  =   db.StringField(max_length = 50)
#     last_name   =   db.StringField(max_length = 50)
#     email       =   db.StringField(max_length = 30)
#     password    =   db.StringField(max_length = 30)


# @app.route("/user")
# def user():
#     User(user_id = 1, first_name = 'Arun', last_name = 'Kumar', email = 'arun@gmail.com', password = '123456').save()
#     User(user_id = 2, first_name = 'Shreya', last_name = 'Swain', email = 'shreya@gmail.com', password = '$123456').save()
#     users = User.objects.all()
#     return render_template('/includes/user.html', users=users)