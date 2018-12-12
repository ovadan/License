import os
from PIL import Image, ImageEnhance
import pytesseract
#import numpy as np
#import cv2

img = Image.open(os.path.expanduser("/Users/Ovadan/Desktop/py/generated_images/image_processed.png"))
text = pytesseract.image_to_string(img, lang='eng')
# print(text)
#text = text.encode('utf-8')

#textEncode = text.encode('utf-8')
print([x for x in text.split('\n')if len(x) == 7])


# print(text.encode('utf-8'))
