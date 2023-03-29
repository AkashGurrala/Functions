#Counting no.of dublicate images between two different folders

import os
train_dir = "C:/Users/z004ns1f/Downloads/FLORA_MAINTENANCE_2_24/dataset/train/" 
test_dir = "C:/Users/z004ns1f/Downloads/FLORA_MAINTENANCE_2_24/dataset/test/"

def similarimagesCount (dir1, dir2):
    foldl = os.listdir(dir1)
    fold2 = os.listdir(dir2)
    result [i for i in fold1 if i in fold2] 
    print(len(result))

similarimagesCount (dir1 train_dir,dir2 test_dir)