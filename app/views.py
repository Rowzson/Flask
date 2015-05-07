# This is views.py

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

#index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Rowson'} #fake name
    return render_template("index.html",title='Home',user=user)

@app.route('/login', methods=['Get','Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',title='Sign in',form=form,providers=app.config['OPENID_PROVIDERS'])
