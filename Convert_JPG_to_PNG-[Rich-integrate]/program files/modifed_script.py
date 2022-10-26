# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2022-10-26 15:40:52

import os
import sys
import PIL
from PIL import Image
import time



UserInput = input("Enter your directory here: ")
target_directory_listdir = os.listdir(UserInput)  # address to script's directory

def saving_images(selectedFiles,saving_directory="D:/Coding_Nerds/FTD/experiment01/M4A1 Arts/converted"):
    


    for file in selectedFiles:
        img = Image.open(f"{UserInput}/{file}")
        img.save(f"{saving_directory}/{file}.png")
        print("File converting => ", file)


def script_Runtime():

    for file in target_directory_listdir:
        if os.path.splitext(file)[1] != ".jpg":  # check if it's a jpg
            files_skipped += 1
            pass
        else:
            files_detected += 1
            selectedFiles.append(file)

    # dont loop. let the magic work.
    saving_images(selectedFiles)



script_Runtime()