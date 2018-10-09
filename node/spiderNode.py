#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import socket,sys
from thread import start_new_thread,exit_thread
import os
import requests
import json
import logging
from formatter import getFormatter
from config import configure
logger = logging.getLogger('spider')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('spider_log/%s' %  time.strftime("%Y-%m-%d.log", time.localtime()) )
handler.setLevel(logging.INFO)
logger.addHandler(handler)

__author__ = 'Lester'

"""
参考 https://www.ctolib.com/topics-86536.html
https://gist.github.com/kevinkindom/108ffd675cb9253f8f71
"""

class Spider:
    """
    爬虫
    """

    def __init__(self,data):
        self.data = data
        # self.status = False # 是否成功访问页面
        # self.content = ''
        # self.statusCode = 0
        # self.url = data['url']
        # self.error = ''
	
	@classmethod
	def validate(cls,data):
		if data['type'] == 'request':
			return True
		return False
		
	
	@classmethod
	def response(cls,url):
		headers = {'user-agent': 'my-app/0.0.1'}
		try:
			r = requests.get(url,headers, timeout=10)
			try:
				requests.Response.raise_for_status()
			except requests.HTTPError,e:
				pass
		except requests.ConnectionError,e:
			pass
		except requests.Timeout,e:
			pass
		except requests.TooManyRedirects ,e :
			pass
		except requests.exceptions.RequestException,e:
			pass
		
    def crawl(self):
        """
        :return: Json 错误信息 或 内容信息
        """
        if self.validate(self.data):
			result = []
			return josn.dumps(result)
		else:
			return json.dumps({
			
			})


class SpiderNode:
    """
    爬虫节点
    """
    max_size = 1024
    port = 9010
    formatter = getFormatter(configure['data_struct'])()

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try:
            self.sock.bind(('',self.port))
        except:
            print "Startup failed. Please check if the port is occupied"
            raise
		cls = getFormatter('json')	
		self.formatter  = cls()


    def run(self):
        self.sock.listen(5)
        while True:
            try:
                conn,addr = self.sock.accept()
                if addr[0] not in ['127.0.0.2','10.10.160.77']:   # IP 判断
                    logger.info( 'Permission denied: Illegal address %s ' % addr[0])
                    raise AddrError('Permission denied: Illegal address')
                logger.info( "Connected by %s:%d" % (addr[0], addr[1]) )
                start_new_thread(self.crawl, (conn,))
            except KeyboardInterrupt:
                logger.info( "connect fail %s:%d " % (addr[0],addr[1]) )
                conn.close()
            except AddrError,e:
                conn.send(e.message)
                conn.close()

    def crawl(self,conn):
        data = ''
        buf = conn.recv(self.max_size)
        data += buf
        while len(buf) == self.max_size:
            buf = conn.recv(self.max_size)
            data += buf
        #print "recv data : %s" % data
        #conn.send('success')
		fdata = self.formatter.decode(data)
		if not fdata:
			conn.send(self.formatter.encode({'type':'dataError','data':data,'error':self.formatter.getStringError()}))
		else:
			response = 
			result = self.formatter.encode( {'url':fdata['url'],
				'statusCode':response.status,
				'content':response.content,
				'error':response.error})
			conn.send(result)
		conn.close()
        print "recv data : %s" % data
        status,data = self.formatter.decode(data)
        if not status :
            conn.send(data)
            conn.close()
        else:
            conn.send(Spider(data).crawl())
            conn.close()
        exit_thread()


if __name__ == '__main__':
    # pass
    # from config import configure
    # print configure
    SpiderNode().run()
