# Cell_Tracking_MT

## Purpose
Live cell microscopy is an essential step in analysing the response of cells to certain drugs which lead to advancements
in finding a cure for deadly diseases such as cancer. In the present master thesis a deep learning solution is proposed
to segment and track cells in microscopy images. The architecture that we propose is based on a DeepSORT tracking
which takes as input detections with bounding boxes from a YOLOv4 architecture and indicates the lineage of cells
present in a well during their life cycle. The research was developed for DIC cell images provided by the Nikon
imaging platform at IBPM-CNR of Rome.

## Methods
![pipeline_bigger_color](https://user-images.githubusercontent.com/24978227/179274935-3dab45fb-4a99-4350-96d9-27f82a6b7127.png)


## Results
### Detection
![yolov4_res](https://user-images.githubusercontent.com/24978227/179275346-8eb61e17-04c6-483b-9478-33619a695440.png)


### Tracking
![tracking_results - Copy](https://user-images.githubusercontent.com/24978227/179274626-2fb0f901-2041-495a-befb-66e92661ea44.png)
