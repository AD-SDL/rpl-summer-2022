''' This code converts the json annotations to YOLO-ready bounding boxes files
The code was found on https://github.com/Unity-Technologies/com.unity.perception/issues/226'''
import json
pic_height = 720
pic_width = 720

with open('./captures_000.json', 'r') as file:
    big_json_file = json.load(file)

for picture in big_json_file['captures']:
    filename = picture['filename'].split('/')[-1]
    filename = filename[:-4] + '.txt'

    
    with open(filename, 'w') as annotation_file:
        for bbox in picture['annotations'][0]['values']:
            annotation_file.write(
                '%d %f %f %f %f\n' % (
                    # Since label_id starts from 1 and yolo starts from 0, this just fixes that. If not fixed, error regarding the number of classes will occur
                    int(bbox['label_id'])-1,
                    (bbox['x'] + bbox['width'] /2)  / pic_width,
                    (bbox['y'] + bbox['height']/2)  / pic_height,
                    bbox['width']                   / pic_width,
                    bbox['height']                  / pic_height
                    )
                )
