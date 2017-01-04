# by theseanco
# Licensed under the WTFPL

print('\033[1m\033[92mGenerator for Arduino to OSC Python scripts\033[0m')

red = '\033[91m'
end = '\033[0m'

# naming the script
scriptName = raw_input(red+'file name (ending in.py):\n'+end)
fileOut = open(str(scriptName), 'w')

# specifying OSC information
ipAddr = raw_input(red+'IP address to send OSC:\n'+end)
port = raw_input(red+'Port to send OSC:\n'+end)

# import python modules
fileOut.write('from time import sleep\nimport OSC\nimport serial\nimport re\n\n')

# import OSC setup
fileOut.write('c = OSC.OSCClient()\nc.connect((\''+ipAddr+'\', '+port+'))\n')
fileOut.write('oscmsg = OSC.OSCMessage()\n\n')

# input and write serial port and baud rate
serialPort = raw_input(red+'Serial port to read:\n'+end)
baudRate = raw_input(red+'Baud rate of Arduino:\n'+end)
fileOut.write('ser = serial.Serial(\''+serialPort+'\', '+baudRate+')\n\n')

# add regex string to ensure serial data isn't garbage - this defaults to msg=
fileOut.write('pattern = re.compile("^msg=")\nsleep(1)\n\n')

# check string
fileOut.write('while True:\n\tt = 0\n\twhile t == 0:\n\t\tcheck = ser.readline()')
fileOut.write('\n\t\tmatched = pattern.match(check)\n\t\tif matched:')
fileOut.write('\n\t\t\tresult = check.split(" ")\n\t\t\tt = 1')
fileOut.write('\n\t\telse:\n\t\t\tprint(\'***DROPPED - GARBAGE DETECTED****\')\n\n')

# specify number of items and the address and data type for each
numItems = int(input(red+'number of values in stream:\n'+end))
itemAddresses = []
itemTypes = []

for i in xrange(numItems):
    fileOut.write('\n\toscmsg = OSC.OSCMessage()')
    address = raw_input(red+'Address for item '+str(i+1)+' (a first / will be added):\n'+end)
    fileOut.write('\n\toscmsg.setAddress(\"/'+address+'\")')
    dataType = raw_input(red+'Data type (str/float/int etc) for item '+str(i+1)+':\n'+end)
    fileOut.write('\n\toscmsg.append('+dataType+'(result['+str(i+1)+']))')
    fileOut.write('\n\tc.send(oscmsg)\n')

print('\033[1m\033[92m!! DONE :) !!\033[0m')
