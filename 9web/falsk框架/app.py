#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
from flask import Flask
from flask import request

app = Flask(__name__)


# Flask自带的Server在端口5000上监听：
@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
	# 需要从request对象读取表单内容：
	if request.form['password'] == '123':
		return '<h3>Hello, ' + request.form['username'] + '!</h3>'
	return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
	app.run()
