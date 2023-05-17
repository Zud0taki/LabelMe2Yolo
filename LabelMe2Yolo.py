import json
import cv2
import glob


def main(img_folder, json_folder, out_folder):
    # variable declaration for the main method
    img_input = []
    json_input = []

    # read images from path
    img_folder = img_folder + "/*.tif"  # TODO: add functionality for more extensions via GUI
    for image in glob.glob(img_folder):
        img_input.append(image)

    # read json files from path
    json_folder = json_folder + "/*.json"  # TODO: add functionality for more extensions via GUI
    for text in glob.glob(json_folder):
        json_input.append(text)

    # check if img_input and json_input have the same length
    if len(json_input) == len(img_input):

        # rewrite json to txt file
        for y in range(len(img_input)):
            with open(json_input[y], 'r') as myfile:
                data = myfile.read()
            img = cv2.imread(img_input[y])
            img_size = img.shape
            txt_name = json_input[y]
            txt_name = txt_name.split("\\")
            txt_name = txt_name[1]
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
            # create new txt_file at output_path
            export_dir = (out_folder + "/" + txt_name + ".txt")
            textfile = open(export_dir, "w")
            for element in annotation_list:
                textfile.write(str(element) + "\n")
            textfile.close()
            export_dir = ""
            annotation_list = []
