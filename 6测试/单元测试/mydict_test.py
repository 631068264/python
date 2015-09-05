#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
import unittest

from mydict import Dict


class TestDict(unittest.TestCase):
	# 以test开头的方法就是测试方法，
	# 不以test开头的方法不被认为是测试方法，测试的时候不会被执行
	#
	# setUp()和tearDown()方法。
	# 这两个方法会分别在每调用一个测试方法的前后分别被执行
	def setUp(self):
		print 'setUp...'

	def tearDown(self):
		print 'tearDown...'

	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEquals(d.a, 1)
		self.assertEquals(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
