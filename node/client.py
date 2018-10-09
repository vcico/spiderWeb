#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
HOST = '127.0.0.1'
PORT = 9010

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# while True:


cmd = raw_input("Please input msg:")
try:
    print 'send'
    s.send(cmd)
    print 'send finish'
    data = s.recv(1024)
    print data
except socket.error, e:
    print 'xxxxxxxxxx'
    print e
    print e.message

    #s.close()