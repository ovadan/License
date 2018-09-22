import os
from PIL import Image, ImageEnhance
import pytesseract
import numpy as np
import cv2

img = Image.open(os.path.expanduser("~/Desktop/py/images/sample.jpg"))
text = pytesseract.image_to_string(img, lang='eng')

print(text)
