import cv2
import csv
import pandas as pd


def draw_bbox(im, xmin, ymin, xmax, ymax, row_nr):
    img = cv2.imread("./B_ok/"+str(im))

    x1 = xmin
    y1 = ymin
    x2 = xmax 
    y2 = ymax
    cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)

    print("print")

    #cv2.imshow('name_of_window', image_to_show)
    cv2.imshow(str(im)+" row: "+str(row_nr+2), img)
    cv2.waitKey()


#goodlabelscsv
#now for the csv  gwgeger
data= pd.read_csv("./videoB_gtruth.csv", delimiter = ';')#delim_whitespace=True)
print(data)

print("Columns: ", data.columns)

print("Rows of image name:", data.image)

image_name = data.image
xmin_line = data.xmin
ymin_line = data.ymin
xmax_line = data.xmax
ymax_line = data.ymax
number_of_rows = len(data.index)

print("nr rows: ", number_of_rows)
print("only names: ", image_name[1])
print("only names: ", image_name[0])

print("random thing", data.image[100])


for line in range(number_of_rows):
    print("Reading line: ", line)
    im = image_name[line]
    xmin = xmin_line[line]
    ymin = ymin_line[line]
    xmax = xmax_line[line]
    ymax = ymax_line[line]
    
    draw_bbox(im, xmin, ymin, xmax, ymax, line)


#VOC to CSV
#merge CSVs
#Clean the damned CSVs
#run this
#create a copy of the damned resulting csv
#label tracking ids there 
