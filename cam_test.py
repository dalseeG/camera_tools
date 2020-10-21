import numpy as np
import cv2 as cv
import time
import smbus

######## I2C Setting ########
# I2C Bus
i2c_ch = 0

# DAC Slave address
i2c_slave = 0x60

# Power Down bits
PD_normal = 0x00

# Bus Initialization
bus = smbus.SMBus(i2c_ch)

def write_dac(value):
	bus.write_byte_data(i2c_slave, PD_normal, value)
	return 0 

######## GUI Setting ########
def on_voltage(val):
	print("voltage %d" % val)
	write_dac(val)

def on_exposure(val):
	print("Exposure %d" % val)

def on_gain(val):
	print("Gain %d" % val)


# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)

cv.namedWindow('frame')

cv.createTrackbar('Film Voltage', 'frame', 0, 255, on_voltage)
cv.createTrackbar('Exposure', 'frame',0, 255, on_exposure)
cv.createTrackbar('Gain', 'frame', 0, 255, on_gain)



while True:

	cv.imshow('frame', img)
	pos = cv.getTrackbarPos('Film Voltage', 'frame')
	font = cv.FONT_HERSHEY_SIMPLEX	
	cv.putText(img, str(pos), (50, 150), font, 6, (255, 255, 255), 10)
	if cv.waitKey(0) == ord('q'):
		break



"""
print("Hello Python")
time.sleep(0.5)
print("Writing DAC values...")
write_dac(0xff)
time.sleep(2)
print("Writing the next DAC values...")
write_dac(0x00)
time.sleep(2)
print("DAC value setting completed")
"""
