####################################################################################################################
#************************************************ images2video ****************************************************# 
####################################################################################################################
# Method: creates a video from multiple images                                                                     #
####################################################################################################################
# Usage: python images2video.py --path C:/Users/Asus/Desktop/ourDataWithoutMarginal/videoA/Images --video vidA.avi #
#------------------------------------------------------------------------------------------------------------------#
# !!!! careful. the slashes must be /. when copy paste it goes \                                                   #
####################################################################################################################
# Utility: for testing YoloV4 and DeepSORT we use videos of the datasets                                           #
####################################################################################################################

import cv2
import os
import argparse

def get_args():
    parser = argparse.ArgumentParser("Movie maker ")
    parser.add_argument(
        "-p",
        "--path",
        "--directory",
        "--folder",
        type=str,
        help="Absolute path for the folder where the images(frames) are located",
    )
    parser.add_argument(
        "--video",
        type=str,
        help="The video's name we are creating",
    )
    args = parser.parse_args()
    return args

def main(opt):
    print("Start making video!")
    
    image_folder = opt.path
    video_name = opt.video
    
    images = [img for img in os.listdir(image_folder) if img.endswith(".tif")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

    print("Finished!")


if __name__ == "__main__":
    options = get_args()
    main(options)