#import FLask class into application

from flask import Flask

#intantiate an object 

app = Flask(__name__)#identify current application /module that is passed through flask.\


from application import routes #seperation of concerns
