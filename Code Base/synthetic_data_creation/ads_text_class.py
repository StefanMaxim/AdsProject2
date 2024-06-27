import cv2
import pprint
import numpy as np
from PIL import Image
from skimage import draw
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

class AdsText:

    fruit_adjective = np.array(["Juicy", "Sweet", "Ripe", "Fresh", "Delicious", "Crisp", ""])
    apple_types = np.array(
        ["Braeburn", "Cameo", "Cox", "Fuji", "Golden Delicious", "Granny Smith", "Jazz", "Pink Crisp", "Red",
         "Royal Gala"])
    oz_bag = np.array(["1 oz bag", "2 oz bag", "3 oz", "4 oz", "5 oz", ""])
    small_prints = np.array(["Northwest grown", "Selected varieties", "Farm raised", "Gluten free", "Previously frozen", ""])

    color_text = (0,0,0)
    text = ""

    font_path = "/Library/Fonts/Supplemental/Arial Bold.ttf"
    font_size =10

    def __init__(self):
        item_adjective = np.random.choice(self.fruit_adjective)
        item_oz = np.random.choice(self.oz_bag)
        item_name = np.random.choice(self.apple_types)
        item_small_prints = np.random.choice(self.small_prints)

        final_text = item_adjective + " " + item_name + "\n" + item_oz + "\n\n" + item_small_prints
        self.text = final_text



    def ads_text_class(self):
        item_adjective = np.random.choice(fruit_adjective)
        item_oz = np.random.choice(oz_bag)

        final_text = item_adjective + " " + item_name + "\n" + item_oz
        self.text = final_text



    def create_text_image(self, img_size, color_background):
        """
        Creates an image of a given size that has the text inside

        :param img_size: the size of the final image
        :param text:
        :param color_background:
        :param color_text:
        :return: the image created from the given text
        """

        new_image = Image.new ('RGB', img_size, color_background)

        # Initialize the drawing context
        draw = ImageDraw.Draw(new_image)

        # Define the font (optional)
        # This is not working for now self.font_size = self.resize_text2(img_size[0], img_size[1])
        font_text = ImageFont.truetype(self.font_path, self.font_size)

        # Define the position where you want to draw the text
        position_text = (3, 10)  # (x, y) coordinates

        # Write the text onto the image
        draw.text(position_text, self.text, fill= (0,0,0), font=font_text)

        return new_image





'''
    def resize_text(self, maxy_width, maxy_height):
        font_size_tmp = 1
        font = ImageFont.truetype(self.font_path, font_size_tmp)
        text_width, text_height = font.getsize(self.text)

        while text_width < maxy_width and text_height < maxy_height:
            font_size_tmp += 1
            font = ImageFont.truetype(self.font_path, font_size_tmp)
            text_width, text_height = font.getsize(self.text)

        return font_size_tmp - 1

    def resize_text2(self, max_width, max_height):
        font_size_crt = 1
        font = ImageFont.truetype(self.font_path, self.font_size)

        # Create a dummy image and draw object to get the text size
        dummy_image = Image.new("RGB", (1, 1))
        dummy_draw = ImageDraw.Draw(dummy_image)

        text_bbox = dummy_draw.textbbox((0,0), self.text, font_size_crt)
        text_width = text_bbox[3] -text_bbox[1]
        print("text width=" + text_width)

           # (dummy_draw.textbbox[3] - dummy_draw.textbbox[1])
        text_height = dummy_draw.textbbox[2] - dummy_draw.textbbox[0]

        while text_width < max_width and text_height < max_height:
            font_size_crt += 1
            font = ImageFont.truetype(self.font_path, font_size_crt)
            text_width = dummy_draw.textbbox[3] - dummy_draw.textbbox[1]
            text_height = dummy_draw.textbbox [2] - dummy_draw.textbbox[0]

        return font


'''