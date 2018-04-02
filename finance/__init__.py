#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/10/14 10:10
@annotation = ''
"""
import os


http = 'http://localhost:8087'
https = 'https://localhost:8087'
os.environ['HTTP_PROXY'] = http
os.environ['HTTPS_PROXY'] = https
