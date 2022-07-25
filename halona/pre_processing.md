# Pre-processing
## Converting the annotation files
https://blog.paperspace.com/train-yolov5-custom-data/
## How to read the json file
It is useful to know that the annotations for multiple images are contained in a json file
* x and y are the coordinates of the top-left of the corner of the binding box
* width and height are the width and height of the bounding box
* If you want to draw a rectangle using cv2 (vision): cv2.rectangle(image, (x,y), (x+width, y+height),color, thickness)
