import cv2
import numpy as np
from matplotlib import pyplot as plt

import os
base_dir = os.path.dirname(os.path.abspath(__file__))

img = cv2.imread(base_dir + "/watch.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)

# https://www.programmersought.com/article/17875689841/
# blocking the program running after the OpenCV window is manually closed
while cv2.waitKey(100) != 27:# loop if not get ESC
  if cv2.getWindowProperty('image',cv2.WND_PROP_VISIBLE) <= 0:
    break
cv2.destroyWindow('image')
