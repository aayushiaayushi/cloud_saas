#! /usr/bin/python

import sys,time,socket,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.10.102"
s_port=8888

s.bind(("",8888))

c_data=s.recvfrom(10)
c_data1=s.recvfrom(10)
print c_data[0]
print c_data1[0]
if c_data[0] == "test" and c_data1[0] == "123":
	print "Authentication successful"
	s.sendto("ok",c_data[1])
else :
	print "Authentication failure"
	exit()
