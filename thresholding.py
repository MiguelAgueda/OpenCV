import cv2
import numpy as np


img = cv2.imread('images/darkImage.jpg', 0)

th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval, threshold = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

cv2.imshow('original', img)
cv2.imshow('adaptive threshold', th)
# cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
