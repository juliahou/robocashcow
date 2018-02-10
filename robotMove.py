import serial

def init(port):
    return serial.Serial(port) # replace with usb port with robot, eg '/dev/tty.usbmodem1421'

def turnRight(ser):
	ser.write(b'r') 
def turnLeft(ser):
	ser.write(b'l') 
def moveForward(ser):
	ser.write(b'f') 
	
def endSesh(ser):
	ser.close()
