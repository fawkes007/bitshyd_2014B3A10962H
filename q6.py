import matplotlib.pyplot as plt
import numpy as np
img = plt.imread('Data for Question 6.jpeg')
plt.hist(n_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

import opencv as opencv
import cv2
from matplotlib import pyplot as plt 
img = cv2.imread('Data for Question 6.jpeg',0)
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(histr) 
plt.show() 
