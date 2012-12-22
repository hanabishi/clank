import sys
import getopt
import time
import wiringpi

DELAY_PWM = 0.020

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

try:
	io.pinMode(1,io.OUTPUT)
	io.digitalWrite(1, io.LOW)
	io.pinMode(1,io.PWM_OUTPUT)

except (KeyboardInterrupt, SystemExit):
	io.pinMode(1,io.OUTPUT)
	io.digitalWrite(1, io.LOW)
i=20
while(1):
	i=i+1
	io.pwmWrite(1, i)
	time.sleep(DELAY_PWM)
	if i>200:
		i=20	

