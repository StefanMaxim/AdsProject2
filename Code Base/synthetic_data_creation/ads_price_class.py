import cv2
import pprint
import numpy as np
from PIL import Image
from skimage import draw
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

class AdsPrice:

    max_currency = 100
    dollar_amount = 1

    cents_selection = np.array(
        [99,97,47,49,99,99,99])
    cents = ""

    color_text = (0,0,0)

    text_selection = np.array(["Member price", " "])
    text = ""

    def __init__(self):
        self.dollar_amount = str (random.randint(1, self.max_currency))
        self.cents = str (np.random.choice(list(self.cents_selection )))
        self.text = np.random.choice(self.text_selection)

    def create_price(self, img_size, color):
        new_image = Image.new('RGB', img_size, color)

        # Initialize the drawing context
        draw = ImageDraw.Draw(new_image)

        # Define the font (optional)
        font_currency = ImageFont.truetype("/Library/Fonts/Supplemental/Arial Black.ttf",
                                           size=30)  # You can specify the path to the font file and font size
        font_cent = ImageFont.truetype("/Library/Fonts/Supplemental/Arial Black.ttf", size=15)
        font_text = ImageFont.load_default(10)

        # Define the position where you want to draw the text
        position_currency = (10, 10)  # (x, y) coordinates
        position_cent = (50, 10)  # (x, y) coordinates
        position_text = (10, 85)  # (x, y) coordinates

        # Define the color of the text (optional)
        color = (0, 0, 0)  # RGB tuple for black color

        # Write the text onto the image
        draw.text(position_currency, self.dollar_amount,  fill=color, font=font_currency)
        draw.text(position_cent, self.cents, fill=color, font=font_cent)
        draw.text(position_text, self.text, fill=color, font=font_text)

        return new_image
        # new_image.show()
