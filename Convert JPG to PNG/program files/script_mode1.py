# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2021-11-05 12:08:40

import os
import sys
import PIL
from PIL import Image

files_detected = 0  # files that are found
files_converted = 0  # files that are converted
files_skipped = 0  # files that does not fit format condition
files_corrupted = 0

target_directory = os.listdir(
    os.path.dirname(sys.argv[0])
)  # address to script's directory

saved_img_folder = "Converted Images"


##############################################################################################33
########################################################


def saving_images(target_file, saving_directory):
    try:
        os.mkdir(saving_directory)
    except FileExistsError:
        print("File converting => ", target_file)
        img = Image.open(target_file)
        img.save(f"{saving_directory}/{os.path.splitext(target_file)[0]}.png")


# you can have a log now!
def save_log(*args):
    with open(f"{saved_img_folder}/Script Log.txt", mode="w") as log_file:
        log_file.write(f"Items Detected - {str(files_detected)} \n")
        log_file.write(f"Images Converted - {str(files_converted)} \n")
        log_file.write(f"Images Skipped - {str(files_skipped)} \n")
        log_file.write(f"Images Found Corrupted - {str(files_corrupted)} \n\n")


for file in target_directory:
    try:
        files_detected += 1
        if file == os.path.basename(
            sys.argv[0]
        ):  # we don't want our file to get edited
            pass
        elif os.path.splitext(file)[1] != ".jpg":  # check if it's a jpg
            files_skipped += 1
            pass
        else:
            files_converted += 1
            saving_images(target_file=file, saving_directory=saved_img_folder)
            save_log(file)

    except PIL.UnidentifiedImageError:  # exception for corrupted image
        print("File", file, "failed to convert")
        files_corrupted += 1
        pass
