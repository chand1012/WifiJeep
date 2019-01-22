#!/usr/bin/python3
import serial
from time import sleep
#arduino = serial.Serial('/dev/ttyACM0', 9600)

def arduwrite():
	sleep(1)
	arduino = serial.Serial('COM4', 9600)
	arduino.write(b'0')
	sleep(1)
	arduino.write(b'1')
	sleep(1)



while True:
	arduwrite()