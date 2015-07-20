################################################################################
# File name: ultrasonic.py
#
# Function: Display the flight height of quadcopter from stm32f4 using Python (matplotlib)
#
# Reference:http://electronut.in/plotting-real-time-data-from-arduino-using-python/
#
################################################################################

import sys, serial
import numpy as np
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
 
# class that holds analog data for N samples
class AnalogData:
# constr
	def __init__(self, maxLen):
		self.d = deque([0.0]*maxLen)
		self.maxLen = maxLen
 
# ring buffer
	def addToBuf(self, buf, val):
		if len(buf) < self.maxLen:
			buf.append(val)
		else:
			buf.pop()
		buf.appendleft(val)
 
#Add new data
	def add(self, data):      
		assert(len(data) == 1)
		self.addToBuf(self.d, data[0])
# plot class
class AnalogPlot:
# constr
	def __init__(self, analogData):
# set plot to animated
		plt.ion()
		plt.figure(figsize=(9,8))
		self.dline, = plt.plot(analogData.d,label="Distance",color="red")
		plt.xlabel("Time")
		plt.ylabel("distance (cm)")
		plt.title("Ultrasonic distance")
		plt.legend()		#Show label figure.
		plt.ylim([0, 2000]) # Vertical axis scale.
		plt.grid()

 
# update plot
	def update(self, analogData):
		self.dline.set_ydata(analogData.d)
		plt.draw()
 
def main():
# expects 1 arg - serial port string
	if(len(sys.argv) != 2):
		print "Type:" 
		print "sudo chmod 777 /dev/ttyUSB0"
		print "python ultrasonic.py '/dev/ttyUSB0'"	# command hint
		exit(1)
 
#strPort = '/dev/tty.usbserial-A7006Yqh'
	strPort = sys.argv[1];

# plot parameters
	analogData = AnalogData(200)  # Horizontal axis scale.
	analogPlot = AnalogPlot(analogData)

	print "plotting data..."
	a = 1
# open serial port
	ser = serial.Serial(strPort, 9600)			# set Baudrate
	while True:
		try:
			line = ser.readline()
			data = [float(val) for val in line.split()]
			if (a < 10):			# to ignore the wrong data that cause the failure while python GUI start
				a = a + 1
			else:
				print data[0]
				if(len(data) == 1):	# number of data sets
					analogData.add(data)
					analogPlot.update(analogData)
		except KeyboardInterrupt:
			print "exiting"
			break
	# close serial
	ser.flush()
	ser.close()
	 
# call main
if __name__ == '__main__':
	main()
