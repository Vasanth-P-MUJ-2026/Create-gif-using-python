# imageio library version 3
# Imageio is a Python library that provides an easy interface to read and write a wide range of image data.
import numpy as np
import imageio.v3 as iio
from PIL import Image

filenames = ['1.png', '2.png', '3.png'] # You can add more PNG files here. Frames will be resized to match the first image.
images = [ ] # 'images' The list containing the image data.

target_size = None

for filename in filenames:
  image = Image.open(filename).convert('RGBA')
  if target_size is None:
    target_size = image.size
  elif image.size != target_size:
    image = image.resize(target_size, Image.Resampling.LANCZOS)
  images.append(np.asarray(image))

# 'penguin.gif' This is the name you want to give to your new GIF file
# 'duration = 500'  How long each picture should show in the GIF, in milliseconds.
# 'loop = 0' How many times the GIF should repeat (0 means it keeps looping forever).
#  The '.imwrite()' method to turn the images into a GIF
iio.imwrite('penguin.gif', images, duration = 500, loop = 0)
