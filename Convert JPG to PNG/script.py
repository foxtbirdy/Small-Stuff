# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2021-11-04 11:35:50

import os
import sys
from PIL import Image


files_detected = 0  # files that are found
files_converted = 0  # files that are converted
files_skipped = 0  # files that does not fit format condition

target_directory = os.listdir(
    os.path.dirname(sys.argv[0])
)  # address to script's directory

saved_img_folder = "wipeout"


def saving_images(target_file, saving_directory):
    try:
        os.mkdir(saving_directory)
    except FileExistsError:
        print("File converting => ", target_file)
        img = Image.open(target_file)
        img.save(f"{saving_directory}/{os.path.splitext(target_file)[0]}.png")


for file in target_directory:
    files_detected += 1
    if file == os.path.basename(sys.argv[0]):  # we don't want our file to get edited
        pass
    elif os.path.splitext(file)[1] != ".jpg":  # check if it's a jpg
        files_skipped += 1
        pass
    else:
        files_converted += 1
        saving_images(target_file=file, saving_directory=saved_img_folder)

# Find all the JPG files

# Create a new folder

# save the files in that folder

print(os.listdir)
print(files_converted)
print(files_skipped)
print(files_detected)

# def folderCreation(fileName):
#   if os.
#
