import pathlib
from PIL import Image
from pathlib import Path

path = str(Path(__file__).parent.absolute())

path_img = path + '/images/'

img = Image.open(path_img + 'pikachu.jpg')
print(img.size)
img.thumbnail((400, 400))
img.save(path_img + 'thumbnail.jpg')
