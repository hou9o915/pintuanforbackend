#!/usr/bin/env python
#-*-coding:UTF-8-*-
from bottle import Bottle,request,jinja2_template as tpl,static_file,debug,abort
from models import *

app = Bottle()

@app.get('/')
def index():
	return '<a href="vida://slideshow?id=12346">Vida</a>'


@app.post('/register')
def register():
	username = request.forms.get('username')
	password = request.forms.get('password')
	try:
		User.get(username=username)
		return tpl('template/failed.tpl',result=0,msg='username has already existed')
	except User.DoesNotExist:
		user = User.create(username=username,password=password)
		return tpl('template/user.tpl',result=1,user=user)


@app.post('/login')
def login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	try:
		user = User.get(username=username,password=password)
		user.update_last_date()
		return tpl('template/user.tpl',result=1,user=user)
	except User.DoesNotExist:
		return tpl('template/failed.tpl',result=0,msg='username or password error')


#@app.get('/activity/recommend')
#def get_ractivity_ecommend():
	