# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2021-11-08 01:53:56

import os
import sys
import PIL
from PIL import Image
import time

files_detected = 0  # files that are found
files_converted = 0  # files that are converted
files_skipped = 0  # files that does not fit format condition
files_corrupted = 0
converted_file_names = []  # list of the converted file names

target_directory = os.listdir(
    os.path.dirname(sys.argv[0])
)  # address to script's directory

saved_img_folder = "Converted Images"

print("Script developed by @Black_2_white. Visit my github for more!!")

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
def save_log(files):
    with open(f"{saved_img_folder}/Script Log.txt", mode="w") as log_file:
        log_file.write(f"Items Detected - {str(files_detected)} \n")
        log_file.write(f"Images Converted - {str(files_converted)} \n")
        log_file.write(f"Images Skipped - {str(files_skipped)} \n")
        log_file.write(f"Images Found Corrupted - {str(files_corrupted)} \n\n")
        log_file.close()

    converted_file_names.append(files)
    with open(f"{saved_img_folder}/Script Log.txt", mode="a") as log_file:
        for file_count in converted_file_names:
            log_file.write(f"{file_count} \n")


print("Program launching in 7 seconds!!!")
time.sleep(7)

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


if files_converted == 0:
    print(
        f"No files were converted. All present {files_detected} files are not .jpg"
        " format"
    )
    time.sleep(3)
elif files_corrupted == 0 and files_converted == 0:
    print(
        f"Script found {files_corrupted}.jpg files that are corrupted. No files"
        " were converted."
    )
else:
    print(f"Program completed converting {files_converted} Files.\nExiting now...")
    time.sleep(2)
