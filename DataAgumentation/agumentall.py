import os 
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import cv2


# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor. 
#I should try and change this 
datagen = ImageDataGenerator(
		rotation_range = 40,
		shear_range = 0.2,
		zoom_range = 0.2,
		horizontal_flip = True,
		brightness_range = (0.5, 1.5))

path = 'D:\curri\sixth\Studying\Pbl\Data\Agumentation\GeneratingDataMenna'    
for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        g_path = os.path.join(root, name) #generated path 
        img= load_img(g_path)
        x = img_to_array(img)
        x = x.reshape((1, ) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size = 1,
        						save_to_dir = 'D:\curri\sixth\Studying\Pbl\Data\Agumentation\Edited',
        						save_prefix ='ed', save_format ='jpeg'):
         	i += 1
         	if i > 5:
                 break
