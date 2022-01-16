from crypt import methods
from turtle import title
from application import app
from application.forms import LoginFrom #since we are importing object from a file named other that (__init__.py) file. we must use folder.filename
from flask import render_template, redirect, flash


@app.route("/")#decorator
def home():
    return render_template("index.html")


@app.route("/login")
def login_():
    form = LoginFrom()
    if form.validate_on_submit():
        flash('Successfully Logged in')
        redirect("/")
    return render_template('/includes/login.html', title="Login", form=form, login=True)

@app.route("/register")
def register():
    return render_template('/includes/register.html')


@app.route("/check-your-health-advanced")
def check_your_health_advanced():
    return render_template('/includes/check-your-health-advanced.html')


@app.route("/check-your-health-common")
def check_your_health_common():
    return render_template('/includes/check-your-health-common.html')


@app.route('/result-check', methods=['POST','GET'])
def result_check():
    return render_template('/includes/result-check.html')


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