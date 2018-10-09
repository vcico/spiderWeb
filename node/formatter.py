#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import json
from abc import ABCMeta, abstractmethod
from validator import Equals,Then,validate,If,Required,Range,InstanceOf,Validator

try:
	from urllib.parse import urlparse
except:
	from urlparse import urlparse

class Url(Validator):
    """
    Use to specify that the
    value of the key being
    validated must be a Url.
    This is a shortcut for saying
    Url().
    # Example:
    validations = {
       "field": [Url()]
    }
    passes = {"field":"http://vk.com"}
    fails  = {"field":"/1https://vk.com"}
    """

    def __init__(self):
    	self.err_message = "must be a valid URL"
        self.not_message = "must not be a valid URL"

    def __call__(self, value):
   		try:
			result = urlparse(value)
			return all([result.scheme, result.netloc])
   		except:
			return False

class Formatter(object):
	"""
	格式化数据基类
	"""

	requestRule = { 
		'url':[Required,Url()]
	}
	responseRule = {
		'url':[Required,Url()],
		'statusCode':[Required,Range(0,505)],
		'content':[Required,InstanceOf(basestring)],
		'error':[InstanceOf(basestring)],
	}
	#dataErrorRule = {
	#	'data':[Required,InstanceOf(basestring)],
	#	'error':[Required,InstanceOf(basestring)]
	#}
	validation = {
		"type":[
			Required,
			If(Equals('request'),Then(requestRule)),
			If(Equals('response'),Then(responseRule)),
			#If(Equals('dataError'),Then(dataErrorRule))
		]
	}

	__instance = None

	def __init__(self):
		self.errors = {} 

	def __new__(cls,*args,**kwargs):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls,*args,**kwargs)
		return cls.__instance

	def	_validate(self,data):
		v = validate(self.validation,data)
		if not v.valid:
			self.errors.update(v.errors)
		return v.valid

	def addError(self,field,errMsg):
		self.errors[field] = errMsg

	def resetError(self):
		self.errors = {}

	@abstractmethod
	def decode(self,data):
		pass		

	@abstractmethod
	def encode(self,data):
		pass

	def getStringError(self):
		return str(self.errors)

class JsonFormatter(Formatter):

	def decode(self,data):
		self.resetError()
		try:
			data = json.loads(data)
		except ValueError , e:
			self.addError('validate',e.message)
			return False
		return data if self._validate(data) else False
	
	def encode(self,data):
		self.resetError()
		if not self._validate(data):
			return False
		return json.dumps(data)

class XmlFormatter(Formatter):

	pass

def getFormatter(f):
	current_module = sys.modules[__name__]
	if not hasattr(current_module,'%sFormatter' % f.capitalize()):
		raise AttributeError('formatter not attribute %s' % f)
	cls = getattr(current_module,'%sFormatter' % f.capitalize())
	return cls

if __name__ == '__main__':
	#getFormatter()
	#cls = '%sFormatter' % 'Json'
	#print	cls()
	#print __module__
	#print	new.instance('JsonFormatter')
	cls = getFormatter('json')
	print cls().encode({'type':'request','url':'http://www.xx.com'})

