# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2022-10-26 20:13:33

import os
import sys
import PIL
from PIL import Image
from rich import print
from rich.progress import Progress
import time
import datetime


now = datetime.datetime.now()
UserInput = input("Enter your directory here: ")



# folder with the current date
saving_dir_default = f"{UserInput}/Converted[{now.strftime('%Y-%m-%d(%H.%M hours)')}]"



def saving_images(file , saving_dir):
    """
    saving the file image
    """
    
    img = Image.open(f"{UserInput}/{file}")
    img.save(f"{saving_dir}/{file}.png")
    print(f"[green]File converted[/] => {file}")




def script_Runtime():
    selectedFiles = []
    for file in os.listdir(UserInput): # probe to given directory
        if os.path.splitext(file)[1] != ".jpg":  # check if it's a jpg
            pass
        else:
            selectedFiles.append(file)


    userChoice = input("\nCreate a new directory? [y/n]: ")
    if userChoice.lower() == "n":
        os.makedirs(saving_dir_default) # creating a new directory
        for file in selectedFiles:
            saving_images(file, saving_dir_default)
    elif userChoice.lower() == "y":
        print("[cyan]This is not built yet")


script_Runtime()



"""
LOGIC

program takes main directory input file converting
program turns all files into png.


"""