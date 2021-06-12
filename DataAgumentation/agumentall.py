import os 
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import cv2

# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor. 
#I should try and change this 

path = "D:\curri\sixth\Studying\Pbl\Data\Agumentation\Edited" #path to the data itself
e_path = "D:\curri\sixth\Studying\Pbl\Data\Agumentation\Edited2" #path to save

#This to create folders from 1 to 29
def one_by_one(value):
    #print(value)
    g_path = []
    lista = [str(k).zfill(2) for k in range(value, value+1)]
    #print(lista)
    for directory in lista:
        parent_dir =e_path
        pa = os.path.join(parent_dir, directory)
        os.mkdir(pa) #now we created for each a file

    #changing parameters changes agumentation
    datagen = ImageDataGenerator(
            rotation_range = 7,
            shear_range = 0.3,
            zoom_range = 0.2,
            horizontal_flip = False,
            vertical_flip = False,
            brightness_range = (0.3, 1.4))

    #load path of each image
    cnt=0
    for root, directories, files in os.walk(path,topdown=True):
        
                
        if cnt==value:
            #print('..................'+str(cnt))
            for name in files:
                g_path.append(os.path.join(root, name)) #generated path
        cnt+=1
    #print(g_path)
    #load image
    for p in g_path:
        img= load_img(p)
        x = img_to_array(img)
        x = x.reshape((1, ) + x.shape)
        i = 0
        for k in lista: #da bta3 el saving
            s_path = '{}/{}'.format(e_path,k)
            
            #print(s_path)            
            for batch in datagen.flow(x, batch_size = 1,
                                    save_to_dir = s_path,
                                    save_prefix ='ed', save_format ='jpeg'):
                i += 1
                if i > 5:
                     break

for i in range(1,30):
    one_by_one(i)
    #print(10*'------')
    


