import serial
from time import sleep
arduino = serial.Serial('/dev/ttyACM0', 9600)

while True:
	arduino.write(b'0')
	sleep(0.05)
	arduino.write(b'1')
	sleep(0.05)
