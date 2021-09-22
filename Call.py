# coding: utf-8
import serial
import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BOARD)

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CMGF=1'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CMGD=1'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CMGR=1'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write("ATD9953154022;"+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
while(1):
	rcv = port.read(10)
	print rcv


