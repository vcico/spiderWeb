#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,request
app = Flask(__name__)

try:
	from urllib.parse import urlparse
except:
	from urlparse import urlparse

cachePath = 'cache/'
hosts = {
	'www.test1.com':'',
	'www.test2.com':'',
	'www.test3.com':'',
	'www.test4.com':'',
}
spiders = [
	(192.168.0.),
]

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>%s host is %s" % (request.url_root,urlparse(request.url_root).netloc)

@app.route("/<path:url>")
def mirror(url):
	return "the url is %s host is %s" % (url,urlparse(request.url_root).netloc)


if __name__ == "__main__":
	    app.run()
