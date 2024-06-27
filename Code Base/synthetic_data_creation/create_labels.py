import numpy as np
from PIL import Image
from skimage import draw
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os
from ads_class import Ads

fruit_adjective = np.array(["Juicy", "Sweet", "Ripe", "Fresh", "Delicious", "Crisp", ""])
apple_types = np.array(["Braeburn", "Cameo", "Cox", "Fuji", "Golden Delicious", "Granny Smith", "Jazz", "Pink Crisp", "Red Delicious", "Royal Gala"])
oz_bag = np.array(["1 oz bag", "2 oz bag", "3 oz", "4 oz", "5 oz", ""])

# picture_pos can be "top, bottom, left or right; text_pos = top ==> price pos = bottom and viceversa

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


def create_price(img_size, dollar_amount, cents, text, color):
    new_image = Image.new('RGB', img_size, color)

    # Initialize the drawing context
    draw = ImageDraw.Draw(new_image)

    # Define the font (optional)
    font_currency = ImageFont.truetype("/Library/Fonts/Supplemental/Arial Black.ttf", size=60)  # You can specify the path to the font file and font size
    font_cent = ImageFont.truetype("/Library/Fonts/Supplemental/Arial Black.ttf", size=30)
    font_text = ImageFont.load_default(10)

    # Define the position where you want to draw the text
    position_currency = (10, 10)  # (x, y) coordinates
    position_cent = (50, 10)  # (x, y) coordinates
    position_text = (10, 85)  # (x, y) coordinates

    # Define the color of the text (optional)
    color = (0, 0, 0)  # RGB tuple for black color

    # Write the text onto the image
    draw.text(position_currency, dollar_amount, fill=color, font=font_currency)
    draw.text(position_cent, cents, fill=color, font=font_cent)
    draw.text(position_text, text, fill=color, font=font_text)

    return new_image
    #new_image.show()

def create_text(item_name):
    """
    Builds a text with randomly selected inputs from a list. This will be used to create the text image of the ads
    :param item_name: 
    :return: a text like Sweet crips apple  3lb bag
    """
    item_adjective = np.random.choice(fruit_adjective)
    item_oz = np.random.choice(oz_bag)

    final_text = item_adjective + " " + item_name + "\n" + item_oz
    return final_text

def create_text_image(img_size, text, color_background, color_text):
    """
    Creates an image of a given size that has the text inside

    :param img_size: the size of the final image
    :param text:
    :param color_background:
    :param color_text:
    :return: the image created from the given text
    """

    new_image = Image.new('RGB', img_size, color_background)

    # Initialize the drawing context
    draw = ImageDraw.Draw(new_image)

    # Define the font (optional)
    font_text = ImageFont.truetype("/Library/Fonts/Supplemental/Arial Bold.ttf", size=9)

    # Define the position where you want to draw the text
    position_text = (3, 10)  # (x, y) coordinates

    # Write the text onto the image
    draw.text(position_text, text, fill=color_text, font=font_text)

    return new_image
    #new_image.show()

def create_one_ad(ads_size, color, position_item, position_price, position_text, input_image_path, output_image_path, output_file_name):
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
    new_image = Image.new('RGB', ads_size, color)

    text = create_text_image(img_size= (100,100), text="Strawberry \n1lb \nRaspberries \n60z selected varieties  \n\nMember price $1 each", color_background=(255,255,255), color_text=(0, 0, 0))
    price = create_price(img_size= (100,100), dollar_amount="1", cents ="99", text="Member price", color=(255,255,0))
    #"/Path/To/input_data/15.jpg"
    item = create_image(image_path=input_image_path, size=(200,150))

    # Paste the JPEG image onto the blank image
    new_image.paste(item, position_item)
    new_image.paste(price, position_price)
    new_image.paste(text, position_text)

    new_image.save(output_image_path + output_file_name + ".png")
    new_image.show()


def create_ads_and_labels(item_image_folder):
    """
    Brief description of the function.

    Detailed description of the function's purpose, parameters, and return value.

    Args:
        item_image_folder: Full path to the folder where we can find the images of the ads.
        arg2: Description of arg2.

    Returns:
        Description of the return value.
    """

    counter = 0
    for file_name in iterate_files(item_image_folder):

        if counter < 1:
            print("Counter:", counter)
            print("filename <" + file_name + ">")

            #Creating ads images
            single_ad = create_one_ad(ads_size = (200,250), color=(255,255,255), position_item = (50, 0),
                                      position_price = (150,150), position_text = (0,150),
                                      input_image_path = item_image_folder + "/" + file_name + ".jpg",
                                      output_image_path = "./out_files/images/", output_file_name = "test" + str(counter) )
            single_ad2 = Ads ()
            single_ad2.print_ads()

            ad_text = create_text("Apple")
            print(ad_text)

            # Creating ads labels



        else:
            return
        counter += 1


def iterate_files(folder_path):
    # Iterate through all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_name_without_extension = os.path.splitext(file_name)[0]
            #yield file_path
            yield file_name_without_extension

create_ads_and_labels("/Path/To/train/images")
#create_one_ad(ads_size = (250,250), color=(255,255,255),position_item = (50, 0), position_price = (150,150), position_text = (0,150) )
#create_text_image(img_size= (150,150), text="Strawberry \n1lb \nRaspberries \n60z selected varieties  \n\nMember price $1 each", color=(255,255,255))
#create_price(img_size= (150,150), dollar_amount="1", cents ="99", text="Member price", color=(255,255,0))
#create_image(image_path="/Users/audbjort/Documents/C_drive/Carmen/_Stefan/code/ads/pythonProject1/ads_project/input_data/15.jpg", size=(300,150))
