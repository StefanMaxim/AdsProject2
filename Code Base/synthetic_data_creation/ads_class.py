import cv2
import pprint
import numpy as np
from PIL import Image
from skimage import draw
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os
from ads_text_class import AdsText
from ads_price_class import AdsPrice


class Ads:
    # Class attributes
    ad_position = (0,0)
    ad_size = (200,200) #width, height
    ad_color = (255, 255, 255)

    #text
    ad_text_size = (100,100)
    ad_text_color = (255, 255, 255)
    ad_text_position = (0, 100)

    #item
    ad_item_color = (255, 255, 255)
    ad_item_size = (200, 100)
    ad_item_position = (0, 0)

    #price
    ad_price_position = (100, 100)
    ad_price_color = (255, 255, 0)
    ad_price_size = (100,100)

    # Constructor method (init method)
    def __init__(self, size= ad_size, image_size = ad_size, text_size = ad_text_size,
                 price_size = ad_price_size,
                 color = ad_color, position_item = ad_item_position, position_price = ad_price_position, text_position = ad_text_position):
        # Instance attributes
        self.ad_size = size
        self.ad_color = color

        self.ad_image_size = image_size
        self.ad_text_size = text_size
        self.ad_price_size = price_size
        self.ad_item_position = position_item
        self.ad_price_position = position_price
        self.ad_text_position = text_position

    # Item - top, text right, price left
    def set_top_right_left(self):
        self.ad_item_position = (0,0)
        self.ad_price_position = (0, 100)
        self.ad_text_position = (100, 100)

    # Item - bottom, text top, price bottom
    def set_left_top_bottom(self):
        self.ad_item_position = (0,0)
        self.ad_item_size = [100, 200]
        self.ad_price_position = (100, 100)
        self.ad_text_position = (100, 0)



    # Instance method
    def instance_method(self):
        return "This is an instance method"

    # Class method
    @classmethod
    def class_method(cls):
        return "This is a class method"

    # Static method
    @staticmethod
    def static_method():
        return "This is a static method"


    def print_ads(self):
        print("AD color: <" + (str)(self.ad_color) + ">" )
        return "This is an instance method"

    def create_one_ad(self, input_image_path,
                      output_image_path, output_file_name):
        '''
        Creates an image of a given size that has the text
        :param ads_size:
        :param color:
        :param position_item:
        :param position_price:
        :param position_text:
        :param image_path: path to the image of the item
        :return:
        '''
        new_image = Image.new('RGB', self.ad_size, self.ad_color)

        #Build the text
        crtText = AdsText()
        text = crtText.create_text_image(self.ad_text_size, self.ad_text_color)

        #Build the price
        crtPrice = AdsPrice ()
        price = crtPrice.create_price(self.ad_price_size, self.ad_price_color)

        item = Image.open(input_image_path)
        item_resized = item.resize(self.ad_item_size)

        new_image.paste(item_resized, self.ad_item_position)
        new_image.paste(price, self.ad_price_position)
        new_image.paste(text, self.ad_text_position)

        new_image.save(output_image_path + output_file_name)
        #new_image.show()


    def label_to_text_mapping (self, label_id):
        '''
        Label 0 = class ads
        Label 1 = class item
        Label 2 = class price
        Label 3 = class text
        :return: respective class
        '''
        if label_id == 0:
            return ("ad", (255, 0, 25))
        if label_id == 1:
            return ("grok", (255, 0, 100))
        if label_id == 2:
            return ("price", (255, 100, 200))
        if label_id == 3:
             return ("text", (173, 255, 47))
        else:
            return ("unknown", (255, 255, 255))


    def build_gt_label(self, output_file):
        '''
        Label 0 = class ads
        Label 1 = class item
        Label 2 = class price
        Label 3 = class text

        output_file = .txt file to write

        For a bounding box wih xmin, xmax, w and h, The normalized formulas:
        x_center = ( xmin +w/2)/w
        y_center = ( ymin +h/2)/h
        normalized_w = w/image_w
        normalized_h = h/image_h

        :return: A file in yolo format with labels
        '''
        f = open(output_file, 'w')

        #ads
        x_center_ad_normalized = (self.ad_position[0] + self.ad_size[0]/2) / self.ad_size[0]
        y_center_ad_normalized = (self.ad_position[1] + self.ad_size[1]/2) / self.ad_size[1]
        width_ad_normalized = self.ad_size[0]/self.ad_size[0]
        height_ad_normalized = self.ad_size[1]/self.ad_size[1]
        f.write("0 " + str(x_center_ad_normalized) + " " + str(y_center_ad_normalized) + " " + str(width_ad_normalized) + " " + str(height_ad_normalized) + "\n")

        #item
        x_center_ad_item_normalized = (self.ad_item_position[0] + self.ad_item_size[0]/2) / self.ad_size[0]
        y_center_ad_item_normalized = (self.ad_item_position[1] + self.ad_item_size[1]/2) / self.ad_size[1]
        width_ad_item_normalized = self.ad_item_size[0]/self.ad_size[0]
        height_ad_item_normalized = self.ad_item_size[1]/self.ad_size[1]
        #x_center_ad_item_normalized = 0.5
        #y_center_ad_item_normalized = 0.25
        #width_ad_item_normalized = 1
        #height_ad_item_normalized = 0.5
        f.write("1 " + str(x_center_ad_item_normalized) + " " + str(y_center_ad_item_normalized) + " " + str(
            width_ad_item_normalized) + " " + str(height_ad_item_normalized) + "\n")

        #price
        x_center_ad_price_normalized = (self.ad_price_position[0] + self.ad_price_size[0]/2) /  self.ad_size[0]
        y_center_ad_price_normalized = (self.ad_price_position[1] + self.ad_price_size[1]/2) /  self.ad_size[1]
        width_ad_price_normalized = self.ad_price_size[0]/ self.ad_size[0]
        height_ad_price_normalized = self.ad_price_size[1]/self.ad_size[1]
        #x_center_ad_price_normalized = 0.75
        #y_center_ad_price_normalized = 0.75
        #width_ad_price_normalized = 0.5
        #height_ad_price_normalized = 0.5
        f.write("2 " + str(x_center_ad_price_normalized) + " " + str(y_center_ad_price_normalized) + " " + str(width_ad_price_normalized) + " " + str(height_ad_price_normalized) + "\n")


        #text
        x_center_ad_text_normalized = (self.ad_text_position[0] + self.ad_price_size[0]/2) / self.ad_size[0]
        y_center_ad_text_normalized = (self.ad_text_position[1] + self.ad_price_size[1] /2) /  self.ad_size[1]
        width_ad_text_normalized = self.ad_text_size[0]/self.ad_size[0]
        height_ad_text_normalized = self.ad_text_size[1] / self.ad_size[1]
        #x_center_ad_text_normalized = 0.25
        #y_center_ad_text_normalized = 0.75
        #width_ad_text_normalized = 0.5
        #height_ad_text_normalized = 0.5
        f.write("3 " + str(x_center_ad_text_normalized) + " " + str(y_center_ad_text_normalized) + " " + str(width_ad_text_normalized) + " " + str(height_ad_text_normalized) + "\n")

    def visualize_gt_labels(self, label_path, image_path):
        # Load the image
        image = cv2.imread(image_path)

        #build labels matrix
        '''
        
        '''
        labels = read_yolo_file(label_path)

        # Loop over the labels
        for label in labels:
            # Extract the class name, confidence score, and bounding box coordinates
            class_name, x, y, w, h = label

            #print("xywh=")
            #print(x, y, w, h )

            # Convert coordinates to integers
            left = int((x - w / 2) * self.ad_size[0])
            top = int((y - h / 2) * self.ad_size[1])
            right = int((x + w / 2) * self.ad_size[0])
            bottom = int((y + h / 2) * self.ad_size[1])

            #print("\n top left botton top=")
            #print(left, top, right, bottom)

            label_text = self.label_to_text_mapping(class_name)[0]
            color_label = self.label_to_text_mapping(class_name)[1]

            # Draw the bounding box and label on the image
            cv2.rectangle(image, (left, top ), (right, bottom), color_label, 2)
            cv2.putText(image, label_text, (left + 10, top + 15 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_label, 2)

        # Show the image
        cv2.imshow("Image with Labels", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def read_yolo_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_matrix = []
    for line in lines:
            line = line.strip().split()
            if len(line) < 5:  # Skip lines without bounding box data
                continue
            class_id = int(line[0])
            x_center = float(line[1])
            y_center = float(line[2])
            width = float(line[3])
            height = float(line[4])
            data_matrix.append([class_id, x_center, y_center, width, height])

    return data_matrix

def create_image(image_path, size):
    # Open the JPEG image
    jpeg_image = Image.open(image_path)

    # Define the new size (e.g., half the original size)
    new_width = jpeg_image.width // 3
    new_height = jpeg_image.height // 2
    resized_image = jpeg_image.resize((new_width, new_height))

    # Create a new blank image
    new_image = Image.new("RGB", size, color="white")

    # Paste the JPEG image onto the blank image
    new_image.paste(resized_image, (0, 0))

    # Save the resulting image
    #new_image.save("output_image_with_jpg_inside.jpg")

    # Display the  image for debugging
    return new_image
    #new_image.show()

from ads_class import Ads
if __name__ == "__main__":
    my_ad = Ads()
    
    REPLACE THE PATH WIHT YOUR OWN
    #test = my_ad.read_yolo_file("...")
    #pprint.pprint(test)

    #create one add
    input_image_path = "..."
    output_image_path ="..."
    output_file_name = "test101"
    #my_ad.create_one_ad (input_image_path, output_image_path, output_file_name)

    #my_ad.build_gt_label("....")


    image_path = "..."
    label_path = "."
    #my_ad.build_gt_label("...")
    #my_ad.visualize_gt_labels(label_path, image_path)