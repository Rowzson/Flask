#This is app inital file from practice1

#from flask import Flask

#app =Flask(__name__)
#from app import views

#This is app inital file from practice3

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
