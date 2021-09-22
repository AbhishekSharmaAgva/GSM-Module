
import serial
import RPi.GPIO as GPIO      
import os, time
def getserial():
	cpuserial = '000000007cab00e5'
	f = open('/proc/cpuinfo','r')
	for line in f:
			if line[0:6]=='serial':
				cpuserial = line[10:26]
				f.close()
				exit()
	return cpuserial
#print(getserial())
if getserial() == '000000007cab00e5':
	print("cpu found")
GPIO.setmode(GPIO.BOARD)    
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
str = chr(26)
while 1:
 
	port.write('AT'+'\r\n')
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)
 
	port.write('AT+CPIN?\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CREG?\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CGATT?\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CIPSHUT\r\n')  # Select Message format as Text mode 
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)
 
	port.write('AT+CIPSTATUS\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CIPMUX=0\r\n')   # New SMS Message Indications
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)
 
# Sending a message to a particular Number
#	port.write("AT+CGDCONT=1"+","+'"IP"'+","'"airtelgprs.com"\r')
#	rcv = port.read(128)
#	print rcv
#	time.sleep(1)

	port.write('AT+CSTT="airtelgprs.com"\r\n')
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CIICR\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CIFSR\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CIPSTATUS\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)

	port.write('AT+CIPSTART="TCP","api.thingspeak.com","80"\r\n')      # Disable the Echo
#	time.sleep(0.3)
	rcv = port.read(128)
	print rcv
	time.sleep(3)

#	port.write('AT+HTTPINIT\r\n')      # Disable the Echo
#	time.sleep(1)
#	rcv = port.read(128)
#	print rcv
#	time.sleep(0.3)


	x='GET https://api.thingspeak.com/update?api_key=FVTA8D044KOWOM7C&field1=10\r\n'
	port.write('AT+CIPSEND\r\n')  # + x +'#026\r')      # Disable the Echo
	rcv = port.read(128)
	print rcv
	time.sleep(0.1)
	port.write(x)
	rcv = port.read(128)
	print rcv
	port.write(str.encode())
	rcv = port.read(128)
	print rcv
 
#	x='GET https://api.thingspeak.com/update?api_key=FVTA8D044KOWOM7C&field1=5000'
	port.write('AT+CIPCLOSE=1'+'\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
        time.sleep(0.1)

#	x='GET https://api.thingspeak.com/update?api_key=FVTA8D044KOWOM7C&field1=5000'
	port.write('AT+CIPSHUT'+'\r\n')      # Disable the Echo
	rcv = port.read(128)
	print rcv
        time.sleep(0.1)

else: 
	cupserial="ERROR000000000"

