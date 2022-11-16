# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"C:\Users\20128\wjpg.jpg")

width, height = im.size

# Setting the points for cropped image
left = 6
top = height / 4
right = 174
bottom = 3 * height / 4


im1 = im.crop((left, top, right, bottom))
newsize = (200, 200)
im1 = im1.resize(newsize)
# Shows the image in image viewer ---------
im1.show()
