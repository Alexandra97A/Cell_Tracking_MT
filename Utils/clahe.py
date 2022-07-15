import numpy as np
import cv2 as cv
from PIL import Image
import glob 
import argparse

count = 1

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
    parser.add_argument(
        "--im_type",
        default="jpg", 
        type=str,
        help="The image's type (tif, jpg)",
    )
    parser.add_argument(
        "--out_path", 
        type=str,
        help="The output directory where the clahe images are stored",
    )
    args = parser.parse_args()
    return args

def main(opt):

    path = opt.path
    im_type = opt.im_type
    print("Start! WE are applying CLAHE twice")
    
    for im in glob.iglob(path+"*."+im_type):
        output_file = opt.out_path
        print(im)
        img = cv.imread(im,0)
        # create a CLAHE object (Arguments are optional).
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        cl2 = clahe.apply(cl1)
        
        #out_img = output_file +im+"."+im_type
        cv.imwrite(im,cl2)
  


    print("Finished!")


if __name__ == "__main__":
    options = get_args()
    main(options)


