#!/usr/bin/python3
#
# Simple test program used for testing
# the new Galaxycore sensor's V4L driver
# and grabbing images for the image
# processing team to analyze
#

import numpy as np
import cv2 as cv


def on_gain(val):
    print("gain %d" % val)

def on_exposure(val):
    print("exposure %d" % val)

def on_voltage(val):
    print("voltage %d" % val)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cv.namedWindow('frame')
cv.createTrackbar('gain', 'frame', 0, 255, on_gain)
cv.createTrackbar('exposure', 'frame', 0, 255, on_exposure)
cv.createTrackbar('film voltage', 'frame', 0, 255, on_voltage)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
