import os
from PIL import Image
from numpy import array
import csv

def img_arr(path, file):
    im_1 = Image.open(r'{}\{}'.format(path, file))
    matt = array(im_1)
    x, y = matt.shape
    mat = list(matt.flatten())  # first matrix
    # print(mat)
    v = (784 - x * y) // 2
    l = [0] * v
    final = l + mat + l  # final centerized matrix
    final = list(map(lambda x: x / 255, final))
    return final, len(final)


def write(value, length, c):
    with open("img_pixels_1.csv", 'a',newline='') as f:
        writer = csv.writer(f)
        # print(value)
        # print([c])
        c = [c] + value
        writer.writerow(c)

c = -1
with open("img_pixels_1.csv", 'a',newline='') as f:
    writer = csv.writer(f)
    f_row = ['label'] + ['pixel{}'.format(i) for i in range(784)]  # first row
    writer.writerow(f_row)

for path, folders, files in os.walk(
        r'F:\E-just\sem 6\PBL\arabic_Data\char_4K_sample\char_sample'):
    c += 1
    print(c)
    for file in files:
        result, length = img_arr(path, file)
        write(result, length, c)