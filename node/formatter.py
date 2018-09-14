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

	def __init__(self):
		self.errors = {} 

	def	_validate(self,data):
		v = validate(self.validation,data)
		if not v.valid:
			self.errors.update(v.errors)
		return v.valid

	def addError(self,field,errMsg):
		self.errors[field] = errMsg

	def resetError(self):
		self.errors = {}

	def getError(self,data):
		"""
		:param data string | dict  解析/编码 的数据
		:return: json
		"""
		strError = ''
		for x,y in self.errors.iteritems():
			strError += " %s : %s , " % (x,y)
		return json.dumps({'type':'dataError','error':strError,'data':data,'info':'data in wrong format'})


	@abstractmethod
	def decode(self,data):
		pass		

	@abstractmethod
	def encode(self,data):
		pass

class JsonFormatter(Formatter):

	def decode(self,jsondata):
		self.resetError()
		try:
			data = json.loads(jsondata)
		except ValueError , e:
			self.addError('validate',e.message)
			return (False,self.getError(jsondata))
		if self._validate(data):
			return (True,data)
		else:
			return (False,self.getError(data))
	
	def encode(self,data):
		self.resetError()
		if not self._validate(data):
			return (False,self.getError(data))
		return (True,json.dumps(data))

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
	pass
	#cls = '%sFormatter' % 'Json'
	#print	cls()
	#print __module__
	#print	new.instance('JsonFormatter')

