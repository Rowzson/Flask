# This is views

#from app import app

#@app.route('/')#for root category
#@app.route('/index')# ***it should be index of website***
#def index():
#    return "hello world"# ***shown strings on the website***

#all the lines above are phase1.

#from flask import render_template
#from app import app

#@app.route('/')
#@app.route('/index')
#def index():
#    user = {'nickname':'Miguel'}#fake user
#    posts = [ #fake array of posts
#        {
#	   'author':{'nickname':'John'},
#  	   'body':'Beautiful day in Portland'
#	},
#	{
#	   'author':{'nickname':'Susan'},
#	   'body':'The Avengers movie wa so cool!'
#	}
#     ]
#    return render_template("index.html",title='Home',
#			   user=user,posts=posts)

#all the lines above are pratice 2

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

#index view function suppressed for brevity

@app.route('/login', methods=['Get','Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data,str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',title='Sign in',form=form)
