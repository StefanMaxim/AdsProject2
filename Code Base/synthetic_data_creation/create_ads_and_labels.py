import cv2
import pprint
import numpy as np
from PIL import Image
from skimage import draw
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os
from ads_class import Ads
from ads_text_class import AdsText
from ads_price_class import AdsPrice

my_ad = Ads()

#Create ads
def create_ads_and_labels_test():
    my_ad = Ads()


    input_image_path = "/Path/To/The/Test.jpg"
    output_image_path = "/Path/To/The/Output/Image.jpg"
    output_file_name = "test101"
    output_ad_path = output_image_path + output_file_name +".png"
    output_label_path = "/Path/To/The/Output/Label"
    output_labels_file = output_label_path + output_file_name + ".txt"

    #Create images
    my_ad.create_one_ad (input_image_path, output_image_path, output_file_name)

    #Create yolo labels
    my_ad.build_gt_label(output_labels_file)

    #Visualize labels
    my_ad.visualize_gt_labels(output_labels_file, output_ad_path )

#Create ads
def create_ads_and_labels():
    my_ad = Ads()
    index_file = ""

    #my_ad.set_top_right_left()

    my_ad.set_left_top_bottom()
    index_file = "ltb_"

    #Training ads
    #input_image_folder = "/Path/To//ads_images_labels/source/training"
    #output_image_folder = "/Path/To//Path/To//ads_images_labels/training/images/"
    #output_label_folder = "/Path/To//ads_images_labels/training/labels/"

    #Testing ads
    #input_image_folder = "/Path/To/ads_images_labels/source/validation"
    #output_image_folder = "/Path/To/ads_images_labels/validation/images/"
    #output_label_folder = "/Path/To/ads_images_labels/validation/labels/"

    #tmp ads for debugging
    input_image_folder = "/Path/To/ads_images_labels/source/tmp"
    output_image_folder = "/Path/To//Path/To/ads_images_labels/tmp/images/"
    output_label_folder = "/Path/To/ads_images_labels/tmp/labels/"

    files = os.listdir(input_image_folder)

    # Filter out directories
    files = [f for f in files if os.path.isfile(os.path.join(input_image_folder, f))]


    # Print the list of files
    print("Files in the folder:")

    counter = 0
    for file in files:
        if counter < 200:
            print(file)

            #File name + extension of the initial image
            image_file = file
            file_name_without_extension = os.path.splitext(os.path.basename(file))[0]

            input_image_path = input_image_folder + "/" + image_file

            # Create images
            my_ad.create_one_ad (input_image_path, output_image_folder, index_file + file)

            # Create yolo labels
            output_labels_file = output_label_folder + index_file + file_name_without_extension + ".txt"
            my_ad.build_gt_label(output_labels_file)

            #visualize labels
            #output_ad_path = output_image_folder + index_file + file
            #my_ad.visualize_gt_labels(output_labels_file, output_ad_path)

        else:
            return
        counter += 1




# Main program logic
if __name__ == "__main__":
    create_ads_and_labels()

























'''
import math  # Importing modules

# Constants
PI = math.pi

# Functions
def calculate_area(radius):
    """Calculate the area of a circle."""
    return PI * radius ** 2

def calculate_circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * PI * radius

class Circle:
    """A class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return calculate_area(self.radius)

    def circumference(self):
        """Calculate the circumference of the circle."""
        return calculate_circumference(self.radius)

# Main program logic
if __name__ == "__main__":
    # Create a Circle object
    circle = Circle(5)

    # Calculate and print the area and circumference of the circle
    print("Circle with radius:", circle.radius)
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())

'''








