#! /usr/bin/python

import sys,time,socket

x= """
press 1 for firefox
press 2 for vlc
press 3 for calculator
press 4 for office 
press 5 for webcam
press 6 for screenshot
"""
print x
ch=raw_input()

if ch == '1':
	print "now wait for sec"
	execfile('firefox.py')

elif ch == '2':
	print "waitin for vlc"
	execfile('vlc.py')
elif ch == '3':
	print "waiting for calculator"
	execfile ('calculator.py')
elif ch == '4':
	print "waiting for opening of LIbreOffice !!!"
	execfile('LibreOffice.py')
elif ch == '5':
	print "Say cheese for Webcam"
	execfile('webcam.py')
elif ch == '6':
	print "Screenshot !!!!"
	execfile('Screenshot.py')
else:
	print "wrong option"
