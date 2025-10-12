from PIL import Image
from sys import argv
import os

images_folder = argv[1]
output_folder = argv[2]
input_format = '.jpg'
output_format = '.png'

# ./images/


def get_input_file_list():
    if os.path.exists(images_folder):
        input_dir = os.scandir(images_folder)
        for entry in input_dir:
            if str.endswith(entry.name, input_format):
                yield entry.name
    else:
        raise Exception('Image Folder does not exist!')


def get_image(name):
    my_image = Image.open(images_folder + name)
    return my_image


for image_name in get_input_file_list():
    image = get_image(image_name)
    output_name = os.path.splitext(image_name)[0] + output_format
    if os.path.exists(output_folder):
        image.save(output_folder + output_name, 'png')
    else:
        os.mkdir(output_folder)
        image.save(output_folder + output_name, 'png')
