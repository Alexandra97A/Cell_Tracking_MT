
python resize.py --path C:/Users/Asus/Desktop/Annotations/vid_A/ImagesNice/ --width 382 --height 320 --im_type tif
python renameFiles.py --path C:/Users/Asus/Desktop/Annotations/vid_A/ImagesNice/ --prefix A
python clahe.py --path C:/Users/Asus/Desktop/Annotations/vid_A/ImagesNice/ 
python images2video.py --path C:/Users/Asus/Desktop/Annotations/vid_A/ImagesNice/ --video vidA.avi