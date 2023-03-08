

pip install easyocr

import matplotlib.pyplot as plt
import cv2
import easyocr
from PIL import Image

import pandas as pd
import regex as re

reader = easyocr.Reader(['en'], gpu = False)

img1 = Image.open("1.png")
img1

result1 = reader.readtext('1.png')
result1

ext_data=[]
for i in result1:
  ext_data.append(i[1])

print(ext_data)
