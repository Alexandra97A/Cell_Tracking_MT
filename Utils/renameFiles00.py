###############################################################################################################
#*********************************************** renameFiles *************************************************# 
###############################################################################################################
# Method: ads a prefix given by string 'pre'                                                                  #
###############################################################################################################
# Usage: python renameFiles.py --path C:/Users/Asus/Desktop/ourDataWithoutMarginal/test/Images --prefix test  #
#-------------------------------------------------------------------------------------------------------------#
# !!!! careful. the slashes must be /. when copy paste it goes \                                              #
###############################################################################################################
# Utility: for YoloV4 we should have pairs of e.g. A1.jpg and A1.txt with annotations                         #
###############################################################################################################


from glob import glob
import os
import argparse

def get_args():
    parser = argparse.ArgumentParser("File renamer ")
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Absolute path for the folder where the files are located",
    )
    parser.add_argument(
        "--pre",
        "--prefix",
        type=str,
        help="The prefix that we want to add",
    )
    args = parser.parse_args()
    return args

def main(opt):
    print("Start!")
    
    count = 1
    directory = opt.path
    pre0 = opt.pre
    pre00 = opt.pre
    
    #insert sorting on directory
    base_path = directory
    files = os.listdir(base_path)


    for i, fp in enumerate(files):
        dst = os.path.join(base_path, pre0+"{0:04d}.jpg".format(i))
        src = os.path.join(base_path, fp) 
        os.rename(src, dst) 
    
    print("Finished!")


if __name__ == "__main__":
    options = get_args()
    main(options)









