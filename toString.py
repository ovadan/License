import os
from PIL import Image, ImageEnhance
import pytesseract
#import numpy as np
import cv2

img = Image.open(os.path.expanduser("~/Desktop/py/images/sampleTH3.jpg"))
text = pytesseract.image_to_string(img, lang='eng')
#text = text.encode('utf-8')

#textEncode = text.encode('utf-8')
print([x for x in text.split('\n')if len(x) == 7])


# print(text.encode('utf-8'))
