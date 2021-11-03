# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2021-11-04 00:50:10

import os
import sys
from PIL import Image, ImageFilter


for file in os.listdir(os.path.dirname(sys.argv[0])):
    if file == os.path.basename(sys.argv[0]):  # we don't want our file to get edited
        pass
    elif os.path.splitext(file)[1] != ".jpg":  # check if it's a jpg
        pass
    else:
        print(file)
        try:
            os.mkdir("converted files")
        except FileExistsError:
            print("Folder already exists")
            img = Image.open(file)
            img.save(f"converted files/{os.path.splitext(file)[0]}.png")


# Find all the JPG files

# Create a new folder

# save the files in that folder

print(os.listdir)


# def folderCreation(fileName):
#   if os.
#
