import json
import cv2
import glob

img_input = []
txt_input = []

for image in glob.glob(
        r"C:\Users\KIZwei\Desktop\People\*.jpg"):  # Dateinamen vom Speicherort auslesen und im Schleifenkörper in einem Array speichern
    img_input.append(image)
for text in glob.glob(r"C:\Users\KIZwei\Desktop\People\*.json"):
    txt_input.append(text)
if len(txt_input) == len(img_input):
    for y in range(len(img_input)):
        with open(txt_input[y], 'r') as myfile:
            data = myfile.read()
        img = cv2.imread(img_input[y])
        img_size = img.shape
        txt_name = txt_input[y]
        txt_name = txt_name.split("\\")
        txt_name = txt_name[5]
        txt_name = txt_name.split(".json")
        txt_name = txt_name[0]
        obj = json.loads(data)
        shape_flag = obj['shapes']
        annotation_list = []
        for x in range(len(shape_flag)):
            points_flag = shape_flag[x]
            points = points_flag['points']
            ul = points[0]
            lr = points[1]
            x_center = lr[0] - ul[0]
            if x_center < 0:
                x_center = ul[0] - lr[0]
            x_addition = 0
            if ul[0] > lr[0]:
                x_addition = lr[0]
            else:
                x_addition = ul[0]
            x_center = int(x_center / 2 + x_addition)
            x_expansion = int(lr[0] - ul[0])
            if x_expansion < 0:
                x_expansion = ul[0] - lr[0]
            x_expansion = x_expansion / img_size[1]
            x_center = x_center / img_size[1]

            y_center = lr[1] - ul[1]
            if y_center < 0:
                y_center = ul[1] - lr[1]
            y_addition = 0
            if ul[1] > lr[1]:
                y_addition = lr[1]
            else:
                y_addition = ul[1]
            y_center = int(y_center / 2 + y_addition)

            y_expansion = int(lr[1] - ul[1])
            if y_expansion < 0:
                y_expansion = ul[1] - lr[1]
            y_expansion = y_expansion / img_size[0]
            y_center = y_center / img_size[0]
            concat = "1 " + str(x_center) + " " + str(y_center) + " " + str(x_expansion) + " " + str(y_expansion)
            annotation_list.append(concat)
        textfile = open(r"C:\Users\KIZwei\Desktop\People\txt" + "/" + txt_name + ".txt", "w")
        for element in annotation_list:
            textfile.write(str(element) + "\n")
        textfile.close()
        annotation_list = []
