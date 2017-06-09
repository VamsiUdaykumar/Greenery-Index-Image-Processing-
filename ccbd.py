import cv2
import numpy as np

img = cv2.imread("cubb.jpg")

    # Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of green color in HSV
lower_green = np.array([0,150,0])
upper_green = np.array([60,255,255])

    # Threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

GREEN_MIN = np.array([0, 150, 0], np.uint8)
GREEN_MAX = np.array([60, 255, 255], np.uint8)

dst = cv2.inRange(res, GREEN_MIN, GREEN_MAX)
no_green = cv2.countNonZero(dst)
print('The number of green pixels in cubbon park: ' + str(no_green))
cv2.namedWindow("opencv")
cv2.imshow('opencv',img)
cv2.waitKey(0)

img = cv2.imread("garden.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([0,150,0])
upper_green = np.array([60,255,255])

mask = cv2.inRange(hsv, lower_green, upper_green)

res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

GREEN_MIN = np.array([0, 150, 0], np.uint8)
GREEN_MAX = np.array([60, 255, 255], np.uint8)

dst = cv2.inRange(res, GREEN_MIN, GREEN_MAX)
no_green1 = cv2.countNonZero(dst)
print('The number of green pixels in my garden: ' + str(no_green1))
print('The Green index = '+str(no_green1/no_green))
print('Let the green scale of cubbon park be 10');
scale=int((no_green1/no_green)*10)
print('From scale of 1-10 the greenery scale of garden compared to cubbon park = '+str(scale));
cv2.namedWindow("opencv")
cv2.imshow('opencv',img)
cv2.waitKey(0)
