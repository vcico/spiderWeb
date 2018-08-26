#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
HOST = '10.10.160.77'
PORT = 9010

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# while True:


cmd = input("Please input msg:")
try:
    print ('send')
    s.send(cmd.encode())
    print ('send finish')
    data = s.recv(1024)
    print (data)
except socket.error as e:
    print ('xxxxxxxxxx')
    print (e)
    print (e.message)

    #s.close()
