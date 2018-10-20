#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,request,redirect,url_for
import os
from functools import wraps


app = Flask(__name__)

app.config [ 'CATCH_DIR'] = '%s/cache/' % os.path.dirname(os.path.realpath(__file__))

try:
	from urllib.parse import urlparse
except:
	from urlparse import urlparse


hosts = {
	'www.test1.com':'http://www.tongxinteng.com/',
	'www.test2.com':'http://muchong.com/',
	'www.test3.com':'http://jandan.net/',
	'www.test4.com':'https://youquhome.com/',
    #https://www.qwyw.org/
    #https://ziranzhi.com/
}

def common(func):
    @wraps(func)
    def wrapper(*args,**kw):
        host = urlparse(request.url_root).netloc
        return func(host,*args,**kw)
    return wrapper

@app.route("/")
@common
def hello(host):
    return "<h1 style='color:blue'>----%s Hello There!</h1>%s host is %s" % (host,request.url_root,urlparse(request.url_root).netloc)


@app.route("/<path:url>")
@common
def mirror(host,url):
    return "the url is %s host is %s" % (url,host)



# @app.before_request
# def before_request():
#     app.host = urlparse(request.url_root).netloc
#     print request.url

if __name__ == "__main__":
    app.run()
