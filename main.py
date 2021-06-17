
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
img_size=28




img_array = cv2.imread(r'F:\E-just\sem 6\PBL\Neual network\arabic\Data\arabic_data\self_made_data\1\1.png', cv2.IMREAD_GRAYSCALE)

new_array = cv2.resize(img_array, (img_size, img_size))
def remove_noise(img):
    l=[]
    for i in img:
        x=list(map(lambda x:(x>10)*x,list(i)))
        l.append(np.array(x))
    return np.array(l)
plt.imshow(remove_noise(new_array),cmap='Greys')
plt.show()