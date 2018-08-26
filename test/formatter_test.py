import unittest
import sys
sys.path.append('/root/spiderWeb')
from node import formatter 
import json

class testFormatter(unittest.TestCase):

	def test_request(self):
		cls = formatter.getFormatter('json')
		f = cls()
		self.assertEquals(f.errors,{})
		self.assertTrue(isinstance(f,formatter.JsonFormatter))
		result = f.decode(json.dumps({
			'type':'request',
			'url':'http://www.baidu.com',
		}))
		print result

	def test_error_request(self):
		cls = formatter.getFormatter('json')
		f = cls()
		#print json.dumps({
		#	'type':'request',
		#	'url':'http://www,baidu.com'
		#})
		print f.decode('{"url": "http://www,baidu.com, "type": "request"}')
		print f.errors

	def test_error_field_request(self):
		cls = formatter.getFormatter('json')
		f = cls()
		print f.decode('{"type":"request","name":"xxx"}')
		print f.errors

	def test_response(self):
		cls = formatter.getFormatter('json')
		f = cls()
		result = f.encode({
			#'type':'response',
			'url':'http://www.baidu.com',
			'statusCode':200,
			'content':'fasfafa'
		})
		print result
		print f.errors

	def test_response_url(self):
		cls = formatter.getFormatter('json')
		f = cls()
		result = f.encode({
			'type':'response',
			'url':'wwwbaiducom',
			'statusCode':600,
			'content':'fasfafa'
		})
		print  result
		print f.errors


if __name__ == '__main__':
	unittest.main()


