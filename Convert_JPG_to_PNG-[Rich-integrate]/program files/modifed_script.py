# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2022-10-26 18:53:08

import os
import sys
import PIL
from PIL import Image
import time
import datetime

now = datetime.datetime.now()
UserInput = input("Enter your directory here: ")

# folder with the current date
saving_dir_default = f"{UserInput}/Converted[{now.strftime('%Y-%m-%d(%H.%M hours)')}]"



def saving_images(file , saving_dir=saving_dir_default):
    """
    saving the file image
    """
    
    img = Image.open(f"{UserInput}/{file}")
    img.save(f"{saving_dir}/{file}.png")
    print("File converted => ", file)




def script_Runtime():
    selectedFiles = []
    for file in os.listdir(UserInput): # probe to given directory
        if os.path.splitext(file)[1] != ".jpg":  # check if it's a jpg
            pass
        else:
            selectedFiles.append(file)

    os.makedirs(saving_dir_default)
    for file in selectedFiles:
        saving_images(file)



script_Runtime()