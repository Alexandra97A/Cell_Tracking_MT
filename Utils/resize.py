##################################################################################################################################
#*************************************************** resize *******************************************************# 
##################################################################################################################################
# Method: resize image/s in a given folder                                                                                       #
##################################################################################################################################
# Usage: python resize.py --path C:/Users/Asus/Desktop/ourDataWithoutMarginal/testResize/ --width 384 --height 320 --im_type jpg #
#--------------------------------------------------------------------------------------------------------------------------------#
# !!!! careful. the slashes must be /. when copy paste it goes \                                                                 #
##################################################################################################################################
# Utility: YoloV4 needs images that has width and height multiples of 32                                                         #
##################################################################################################################################

from PIL import Image
import glob 
import argparse


def get_args():
    parser = argparse.ArgumentParser("Image resizer ")
    parser.add_argument(
        "--path",
        type=str,
        help="Absolute path for the folder where the images(frames) are located",
    )
    parser.add_argument(
        "--width",
        default=384,  #multiple of 32; 32*12 = 384
        type=int,
        help="The image's width (x)",
    )
    parser.add_argument(
        "--height",
        default=320, 
        type=int,
        help="The the image's height (y)",
    )
    
    parser.add_argument(
        "--im_type",
        default="tif", 
        type=str,
        help="The image's type (tif, jpg)",
    )
    args = parser.parse_args()
    return args

def main(opt):
    print("Start resizing image!")
    
    path = opt.path
    width = opt.width
    height = opt.height
    im_type = opt.im_type
    zero0 = " "
    zero1 = "0"
    zero2 = "00"
    zero3 = "000"
    zero4 = "0000"
    print("path: ", path)
    count = 1

    for im in glob.iglob(path+"*."+im_type):
        print(im)
        image = Image.open(im)
        new_image = image.resize((width, height))
        #if count < 10:
        #    new_image.save( zero4+'%d' %count + '.tif')
        #elif count >= 10 and count < 100:
        #    new_image.save( zero3+'%d' %count + '.tif')
        #elif count >= 100 and count < 1000 :
        #    new_image.save( zero2+'%d' %count + '.tif')
        #elif count >= 1000 and count < 10000:
        #    new_image.save( zero1+'%d' %count + '.tif')
        
        if count < 10:
            new_image.save( zero4+'%d' %count + '.jpg')
        elif count >= 10 and count < 100:
            new_image.save( zero3+'%d' %count + '.jpg')
        elif count >= 100 and count < 1000 :
            new_image.save( zero2+'%d' %count + '.jpg')
        elif count >= 1000 and count < 10000:
            new_image.save( zero1+'%d' %count + '.jpg')
        count = count + 1

    print(count)
    print('done')

    print("Finished!")


if __name__ == "__main__":
    options = get_args()
    main(options)