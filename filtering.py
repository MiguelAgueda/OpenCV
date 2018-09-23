import cv2
import numpy as np


plum = cv2.imread('plum.png')

# while True:
hsv = cv2.cvtColor(plum, cv2.COLOR_BGR2HSV)

lower_red = np.array([30, 150, 50])
upper_red = np.array([255, 255, 180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(plum, plum, mask=mask)

cv2.imshow('plum', plum)
cv2.waitKey(0)
cv2.destroyAllWindows()
