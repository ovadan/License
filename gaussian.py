import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread(os.path.expanduser("~/Desktop/py/1235.jpg"), 0)
th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 2)
cv.imwrite("testing2G.jpg", th)
