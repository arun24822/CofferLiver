#import FLask class into application

from flask import Flask
# from mongoengine.connection import connect
# from config import Config
# from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os


#intantiate an object 

app = Flask(__name__)#identify current application /module that is passed through flask.\
# app.config.from_object(Config)
# db = MongoEngine()
# db.init_app(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'coffer.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) #db is the sqlalchemy object.
marsh = Marshmallow(app)
jwt = JWTManager(app)

from application import routes #seperation of concerns
from application import api

