from time import sleep
import OSC
import serial
import re

c = OSC.OSCClient()
c.connect(('127.0.0.1', 57120))
oscmsg = OSC.OSCMessage()

ser = serial.Serial('/dev/ttyACM0', 115200)

pattern = re.compile("^msg=")
sleep(1)

while True:
	t = 0
	while t == 0:
		check = ser.readline()
		matched = pattern.match(check)
		if matched:
			result = check.split(" ")
			t = 1
		else:
			print('***DROPPED - GARBAGE DETECTED****')


	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress("/val1")
	oscmsg.append(int(result[1]))
	c.send(oscmsg)

	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress("/val2")
	oscmsg.append(int(result[2]))
	c.send(oscmsg)
