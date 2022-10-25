'''
IMAGE RESIZER DIRECTORY

'''


from PIL import Image
import os, sys

path = "/Users/air/Downloads/Resize_png/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((150, 150), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', 'png', quality=90)

resize()