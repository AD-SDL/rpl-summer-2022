# Requirements:
* Shapes
* Location
* Size
* Color (not necessary)
## YOLO:
YOLO is extremely fast (45 frames per second) than other object detection algorithms because it uses frame detection as a regression problem so we do not need a complex pipeline. It reasons globally about the image when making predictions and sees the entire image during training and test time. It also learns generalizable representations of objects. 

One drawback is that it lags behind state-of-the-art detection systems in accuracy. This shouldn’t be a major problem because we do not want to measure anything but just detect the pipette. Another drawback is that struggles with small objects within the image because of the spatial constraint of the algorithm. This will be a problem for us if we choose to detect residues in the pipette. 

### YOLOx:
YOLO can work well for multiple objects where each object is associated with one grid cell. But in the case of overlap, in which one grid cell actually contains the centre points of two different objects, we can use something called anchor boxes to allow one grid cell to detect multiple objects.

YOLO works well for mutiple objects associated with one grid cell because of anchor boxes. In the case of overlap of objects in one grid cell, YOLO uses something called anchor boxes. YOLOx DOES NOT have anchor boxes, thus reduces the cost of putting anchor boxes.
### StreamYOLO:
SteamYOLO can be used for Real-time Object Detection for Streaming Perception
![image](https://user-images.githubusercontent.com/72309881/177625358-48aaae76-6927-4bd8-b874-329e0952fdce.png)

https://github.com/yancie-yjr/StreamYOLO

## RCNN? 
RCNN takes a huge amount of time and cannot be implemented in real time. Also, the search algorithm is fixed so there’s no learning there. 

https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e 

## Final pre-trained model:
Yolov5 was chosen because it is the newest version of the Yolo. We ended up choosing Yolov5m (m stansds for medium). Future scope: can test how much slower Yolov5l and Yolov5xl is. 
https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data
