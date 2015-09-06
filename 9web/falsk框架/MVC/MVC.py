#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
from flask import Flask, request, render_template, flash

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == 'password':
		return render_template('signin-ok.html', username=username)
	else:
		flash("粗无")
		return render_template('form.html', username=username)


if __name__ == '__main__':
	app.run(debug=True)

"""
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
"""
