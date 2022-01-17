from turtle import title
from application import app
from application.forms import LoginFrom #since we are importing object from a file named other that (__init__.py) file. we must use folder.filename
from flask import render_template, redirect, flash, request
import numpy as np
import joblib


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
    if request.method == "POST":
        age = request.form.get("age-c")
        gender = request.form.get("gender-c")
        alb = request.form.get("alb")
        alp = request.form.get("alp")
        alt = request.form.get("alt")
        ast = request.form.get("ast")
        bil = request.form.get("bil")
        che = request.form.get("che")
        chol = request.form.get("chol")
        crea = request.form.get("crea")
        ggt = request.form.get("ggt")
        prot = request.form.get("prot")      

        if gender == "Male":
            gender = 0
        else:
            gender = 1
        print("#######")
        print(gender)  

        to_predict_list = [age, gender, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot]
        prediction = Predictor(to_predict_list)
        probabilty_list = ProbabiltyPredictor(to_predict_list)
        [[one, two, three, four, five]] = probabilty_list
        return render_template('/includes/result-check.html', prediction=prediction, nofattyliver=one, fattyliver=two, hepatitis=three, fibrosis=four, cirrhosis=five)


def Predictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,-1)
    print(to_predict)
    loaded_model = joblib.load("saved_model")
    result = loaded_model.predict(to_predict)
    return str(result[0])

def ProbabiltyPredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,-1)
    loaded_model = joblib.load("saved_model")
    probabilty_list = loaded_model.predict_proba(to_predict)
    return (probabilty_list)


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

