import easyocr


def detect():
    image_folder = ""

def test():
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])  # You can specify additional languages if needed

    # Perform OCR on the image
    result = reader.readtext('Path/To/The/jpg')

    # Display the result
    for detection in result:
        print(detection[1])  # Text detected


# Main program logic
if __name__ == "__main__":
    test()