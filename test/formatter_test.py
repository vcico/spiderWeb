import unittest
import sys
sys.path.append('C:\projects\spiderWeb')
from node import formatter
import json

class testFormatter(unittest.TestCase):

	format = formatter.getFormatter('json')()

	def test_request(self):
		self.assertEquals(self.format.errors,{})
		self.assertTrue(isinstance(self.format,formatter.JsonFormatter))
		result = self.format.decode(json.dumps({
			'type':'request',
			'url':'http://www.baidu.com',
		}))
		print result

	def test_error_request(self):
		print self.format.decode('{"url": "http://www,baidu.com, "type": "request"}')
		print self.format.errors

	def test_error_field_request(self):
		print self.format.decode('{"type":"request","name":"xxx"}')
		print self.format.errors

	def test_response_error(self):
		result = self.format.encode({
			#'type':'response',
			'url':'http://www.baidu.com',
			'statusCode':200,
			'content':'fasfafa'
		})
		print result
		print self.format.errors

	def test_response_url(self):
		result = self.format.encode({
			'type':'response',
			'url':'wwwbaiducom',
			'statusCode':600,
			'content':'fasfafa'
		})
		print  result
		print self.format.errors
		
	def test_response(self):
		result = self.format.encode({
			'type':'response',
			'url':'http://www.baidu.com',
			'statusCode':200,
			'content':'right'
		})
		print  result
		print self.format.errors


if __name__ == '__main__':
	unittest.main()


