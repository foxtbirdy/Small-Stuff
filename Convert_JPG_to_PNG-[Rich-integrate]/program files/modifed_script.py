# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2022-10-27 03:57:28

import os
import sys
import PIL
from PIL import Image
from rich import print
from rich.progress import Progress
import time
import datetime


def saving_images(file_list , saving_dir):
    """
    saves file image from a given directory.
    """
    for file in file_list:
        img = Image.open(f"{target_dir}/{file}")
        img.save(f"{saving_dir}/{file}.png")
        print(f"[green]File converted[/] => {file}")


def scan_dir(target_dir):
    """
    scan of the directory + validation for script runtime
    """

    # restart the values
    selectedFiles = []
    files_selected = 0
    files_skipped = 0
    files_detected = 0

    for file in os.listdir(target_dir):
        files_detected+=1
        if os.path.splitext(file)[1] == ".jpg":  # check if it's a jpg
            selectedFiles.append(file)
            files_selected+=1
        else: # file is not jpg, then skip
            files_skipped+=1
            pass

    print(f"total selected files: {files_selected}")
    print(f"total skipped files: {files_skipped}")
    print(f"total detected files: {files_detected}")

    return selectedFiles

def script_Runtime(target_dir):
    userChoice = input("\nCreate a new directory? [y/n]: ")

    if userChoice.lower() == "n": # save all files on the target directory
        saving_images(scan_dir(target_dir), saving_dir=target_dir)
        print(f"Files saved at [i][blue]{target_dir}[/]")

    elif userChoice.lower() == "y": # save all files on a new given directory
        saving_dir = input("Enter new directory for saving files: ")
        os.makedirs(saving_dir)
        saving_images(scan_dir(target_dir), saving_dir)




while True:
    target_dir = input("Enter your directory here: ")
    if len(scan_dir(target_dir)) == 0: # if length of selected files is 0, continue loop.
        print("[red]Warning: No images found to convert to png[/]\n[yellow]Try Again.[/]")
    elif len(scan_dir(target_dir)) > 0: # if length of selected files is not 0, break loop after saving
        print("[green]Images found")
        script_Runtime(target_dir)
        break

