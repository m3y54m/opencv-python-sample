import cv2
import numpy as np
from matplotlib import pyplot as plt

import os
base_dir = os.path.dirname(os.path.abspath(__file__))

img = cv2.imread(base_dir + "/watch.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
