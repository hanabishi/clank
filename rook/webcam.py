import cv
from socket import *
import sys
import getopt

try:
	PORT=int(sys.argv[1])
except:
	print "Script requires a port number for the server as argument.\n"
	sys.exit(2)

HOST = '0.0.0.0'
ADDR = (HOST,PORT)
BUFSIZE = 4096
serv = socket( AF_INET,SOCK_STREAM)    
serv.bind((ADDR))    #the double parens are to create a tuple with one element
serv.listen(5)    #5 is the maximum number of queued connections we'll allow
while(1):
	conn,addr = serv.accept()
	try:
		for i in range(10):
			capture = cv.CaptureFromCAM(i)
			if(capture):
				cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 1440)
				cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 1080)
				cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_BRIGHTNESS,128)
				cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_CONTRAST,128)
				frame = cv.QueryFrame(capture)
				cv.SaveImage("tmp.png",frame)
				del(capture)
				with open('tmp.png','r') as f:
					conn.send(f.read())
				break
	finally:
		conn.close()

