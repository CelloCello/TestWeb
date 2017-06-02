# -*- coding: utf-8 -*-

from flask import Flask, url_for, redirect, render_template, flash, request, session
#app = Flask(__name__)


# configuration
DEBUG = True
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def index():
	flash('test')
	return render_template('index.html')
	
@app.route('/hello')
def hello():
	rst_ = "This is Hello World page!" + "<br>"
	rst_ = rst_ + url_for('hello')
	print url_for('hello',para='tst')
	#print url_for('hello')
	return rst_
	
	
if __name__ == '__main__':
	app.debug = True
	app.run()
