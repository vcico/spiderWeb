#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import socket,sys
from thread import start_new_thread,exit_thread
import os
import requests
import json


__author__ = 'Lester'

"""
参考 https://www.ctolib.com/topics-86536.html
https://gist.github.com/kevinkindom/108ffd675cb9253f8f71
"""

class AddrError(Exception):
    """Base class for exceptions in this module."""
    pass

class Response(object):
    """
    采集结果
    """
    __slots__ = ('url', 'statusCode','content','error','data')

    def __init__(self,data):
        # self._result = {}
        self.init(data)

    def init(self,data):
        try:
            data = json.loads(data)
        except ValueError,e:
            self.data = data
            self.error = 'The format of the request is incorrect'


class Spider:
    """
    爬虫
    """

    def crawl(self,data):
        pass

class SpiderNode:
    """
    爬虫节点
    """
    max_size = 1024
    port = 9010

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try:
            self.sock.bind(('',self.port))
        except:
            print "Startup failed. Please check if the port is occupied"
            raise


    def run(self):
        self.sock.listen(5)
        while True:
            try:
                conn,addr = self.sock.accept()
                if addr[0] not in ['127.0.0.2']:   # IP 判断
                    print 'Permission denied: Illegal address'
                    raise AddrError('Permission denied: Illegal address')
                print "Connected by %s:%d" % (addr[0], addr[1])
                start_new_thread(self.crawl, (conn,))
            except KeyboardInterrupt:
                print "connect fail %s:%d " % (addr[0],addr[1])
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
        print "recv data : %s" % data
        conn.send('success')
        conn.close()
        exit_thread()


if __name__ == '__main__':
    SpiderNode().run()
