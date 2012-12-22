import smbus
import time
#import i2c
import quick2wire.i2c as i2c

def i2c_example():
    #PORTS 5V, ground
    #15,16  GIPO 0 (SDA), GIPO 1 (SCL)
    #http://www.skpang.co.uk/blog/archives/575
    bus = smbus.SMBus(1)
    address = 0x20
    i = 0
    while True:
        bus.write_byte(address,i^0xff)
        print bus.read_byte(address)^0xff
        i+=1
        time.sleep(1)

def servo_example():
    servos = i2c.I2C()
    servos.setSpeeds(100,-100)
    servos.setPWM(15,4095)
    
if __name__ == "__main__":
    servo_example()