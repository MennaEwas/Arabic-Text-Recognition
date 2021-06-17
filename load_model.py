import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
from numpy import asarray
import numpy as np
import cv2

# # load the image
# image = Image.open('pic_.png')
# # convert image to numpy array
# data1 = asarray(image)
# image = Image.open('1.png')
# data2 = asarray(image)

img_size=28
img_array = cv2.imread('36.png', cv2.IMREAD_GRAYSCALE)
new_array = cv2.resize(img_array, (img_size, img_size))

img_array = cv2.imread('39.png', cv2.IMREAD_GRAYSCALE)
new_array2 = cv2.resize(img_array, (img_size, img_size))
print(new_array2)
def remove_noise(img):
    l=[]
    for i in img:
        x=list(map(lambda x:(x>180)*x,list(i)))
        l.append(np.array(x))
    return np.array(l)
print('-'*50)
print(remove_noise(new_array2))

test=[new_array,new_array2]
test=[remove_noise(new_array),remove_noise(new_array2)]
test=np.array(test)

plt.imshow(new_array2)
plt.show()
plt.imshow(remove_noise(new_array2))
plt.show()



# mnist=tf.keras.datasets.mnist
# (x_t,y_t),(x_test,y_test)=mnist.load_data()
# print(x_test[:1])
# # print(len(x_test))
# print('-'*12)
# print(test[:1])
# plt.imshow(x_test[0])
# plt.show()









# test=tf.keras.utils.normalize(test,axis=1)
# print()

new_model=tf.keras.models.load_model('segmented_letters.model')
# predections=new_model.predict([test])
# print(predections)
# print(np.argmax(predections[0]))