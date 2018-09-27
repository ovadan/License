import os
from PIL import Image, ImageEnhance
import pytesseract
import numpy as np
import cv2

#from PIL import Image


#img = Image.open("testing.jpg")
#text = pytesseract.image_to_string(img, lang='eng')
img = cv2.imread(os.path.expanduser("~/Desktop/py/images/sample.jpg"), 0)
ret, thresh = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('image', thresh)
cv2.imwrite("sampleTH3.jpg", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
#contrast = ImageEnhance.Contrast(img)
# img.show()
# contrast.enhance(2).show()

#contrast = contrast.enhance(FACTOR)
#img_array = np.array(contrast.getdata())


# print(text)
# img.show()

#im = Image.open("1.jpg").convert("L")
# print(img.format)
# print(img.mode)


#funct1 = open("myfile.txt", "r")
# print(funct1.read())
# funct1.close()
