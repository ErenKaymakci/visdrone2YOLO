import os 
from PIL import Image 
import argparse

LABELPATH = "VisDrone-Labels"
OUTLABELPATH = "YOLO-Labels"
IMAGEPATH = "VisDrone-Images"

def convertYOLO(labels = tuple(), filename= ''):
    # labels contains bbox top-left x and y coordinates, width, height, class
    x, y, width, height, classIdx = labels
    
    img_path = os.path.join(IMAGEPATH, filename[:-3] + "jpg")
    img = Image.open(img_path)
    image_width, image_height = img.size

    x_center = x + (width / 2) 
    y_center = y + (height / 2)
    yoloX = round(x_center / image_width, 6)
    yoloY = round(y_center / image_height, 6)
    yoloW = round(width / image_width, 6)
    yoloH = round(height / image_height, 6)
    print(yoloX, yoloY, yoloW, yoloH)

    return (classIdx - 1, yoloX, yoloY, yoloW, yoloH)

def writeYOLO(YOLOresults, filename):
    txt_path = os.path.join(OUTLABELPATH, filename)
    
    f = open(txt_path, 'a')
    f.write(f"{YOLOresults[0]} {YOLOresults[1]} {YOLOresults[2]} {YOLOresults[3]} {YOLOresults[4]}\n")

def parseVisLine(line):
    parsed = line[:-5].split(",")

    # bounding box top-left coordinates
    x = int(parsed[0])
    y = int(parsed[1])

    width = int(parsed[2])
    height = int(parsed[3])
    class_indx = int(parsed[5])

    return (x, y, width, height, class_indx)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ignore', type=bool, required=False, default=False)
    args = parser.parse_args()
    ignore = args.ignore

    labelFiles = os.listdir(LABELPATH)

    if labelFiles == None:
        pass # VisDrone Label file is empty ! 

    lines = []
    print(labelFiles)
    for txt in labelFiles:
        for line in open(os.path.join(LABELPATH, txt)).readlines():
            elems = parseVisLine(line)
            if ignore:
                if elems[4] == 0 or elems[4] == 11:
                    continue
                    
            results = convertYOLO(elems, txt)
            writeYOLO(results,txt)


if __name__ == '__main__':
    main()
    