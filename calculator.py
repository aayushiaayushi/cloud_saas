#! /usr/bin/python

import os,socket,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.10.102"
s_port=8888

os.system('ssh -X test@'+s_ip+' gnome-calculator')
execfile('saas.py')
