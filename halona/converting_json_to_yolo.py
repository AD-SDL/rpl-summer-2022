''' This code converts the json annotations to YOLO-ready bounding boxes files
The code was found on https://github.com/Unity-Technologies/com.unity.perception/issues/226'''
import json
pic_height = 680
pic_width = 680

with open('./captures_000.json', 'r') as file:
    big_json_file = json.load(file)

for picture in big_json_file['captures']:
    filename = picture['filename'].split('/')[-1]
    filename = filename[:-4] + '.txt'

    with open(filename, 'w') as annotation_file:
        for bbox in picture['annotations'][0]['values']:
            annotation_file.write(
                '%d %f %f %f %f\n' % (
                    bbox['label_id'],
                    (bbox['x'] + bbox['width'] /2)  / pic_width,
                    (bbox['y'] + bbox['height']/2)  / pic_height,
                    bbox['width']                   / pic_width,
                    bbox['height']                  / pic_height
                    )
                )
