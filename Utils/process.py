import glob
import os
import numpy as np
import sys

current_dir = r"C:\Users\Asus\Desktop\ourDataWithoutMarginalwithIgni\cell_images"
folder_name = "cell_images"
split_pct = 10;
file_train = open("train.txt", "w")  
file_val = open("test.txt", "w")  
counter = 1  
index_test = round(100 / split_pct)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_val.write("/content/gdrive/My Drive/yolov4_cells/darknet/data/" + folder_name + "/" + title + '.jpg' + "\n")
    else:
        file_train.write("/content/gdrive/My Drive/yolov4_cells/darknet/data/" + folder_name + "/" + title + '.jpg' + "\n")
        counter = counter + 1
file_train.close()
file_val.close()