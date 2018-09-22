import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread(os.path.expanduser("~/Desktop/py/images/sample.jpg"), 0)
ret, th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("sampleG.jpg", thresh)
