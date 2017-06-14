#! /usr/bin/python

import sys,time,socket,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.10.102"

s_port=8888
#user name on server
s_user=raw_input("enter user name :")
#passsword on server
s_passwd=getpass.getpass("enter password:")

s.sendto(s_user,(s_ip,s_port))
s.sendto(s_passwd,(s_ip,s_port))

data=s.recvfrom(10)
if data[0] == "ok":
	print "successful"
	execfile('saas.py')	
else:
	print "unsussecful"


