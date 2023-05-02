"""
    - Import Python Imaging Library (PIL) module to manipulate images.
    - Import Image class which provides methods for opening, minpulatin and saving image files.
    - Import file dialog module that provides a method for selecting files using a graphical interface.
    - Define function compressor() that do the following:
        1- Open a file dialog box that allows the user to select an image and store its path in file_path.
        2- Open a file image located at file_path and store it in the img variable.
        3- Retrieve the size of the image (height, width).
        4- Resize the image and ask the user the write the name of the compressed image.
    Note: that program works only with the image extensions that Pillow library provides.
"""
import PIL
from PIL import Image
from tkinter.filedialog import *

def compressor():
    file_path = askopenfilename()
    img = PIL.Image.open(file_path)
    file_extension = file_path.split('.')[-1]
    height, width = img.size
    img = img.resize((height, width), PIL.Image.BOX)
    save_path = asksaveasfilename(defaultextension=file_extension)
    img.save(save_path, optimize = True)

compressor()