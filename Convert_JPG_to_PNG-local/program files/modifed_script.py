# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-11-03 19:59:47
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-30 15:09:09

import os
import sys
import PIL
from PIL import Image
import time



UserInput = input("Enter your directory here: ")
target_directory_listdir = os.listdir(UserInput)  # address to script's directory
saved_img_folder = f"{UserInput}/ConvertedFiles"


def saving_images(selectedFiles, saving_directory):
    for file in selectedFiles:
        print("File converting => ", file , saving_directory)
        img = Image.open(f"{UserInput}/{file}")
        img.save(f"{saving_directory}/{file}.png")


def save_log(file, files_detected, files_converted, files_skipped, files_corrupted, convertedFile_named, saved_img_folder):
    with open(f"{saved_img_folder}/Script Log.txt", mode="w") as log_file:
        log_file.write(f"Items Detected - {str(files_detected)} \n")
        log_file.write(f"Images Converted - {str(files_converted)} \n")
        log_file.write(f"Images Skipped - {str(files_skipped)} \n")
        log_file.write(f"Images Found Corrupted - {str(files_corrupted)} \n\n")
        log_file.close()

    convertedFile_named.append(file)
    with open(f"{saved_img_folder}\\Script Log.txt", mode="a") as log_file:
        for file_count in convertedFile_named:
            log_file.write(f"{file_count} \n")


def script_Runtime():
    files_detected = 0  
    files_converted = 0  
    files_skipped = 0  
    files_corrupted = 0
    selectedFiles = [] # files that are selected for converting
    convertedFile_named = [] # files that are already converted

    for file in target_directory_listdir:
        if file == os.path.basename(sys.argv[0]):  # we don't want our file to get edited
            pass
        elif os.path.splitext(file)[1] != ".jpg":  # check if it's a jpg
            files_skipped += 1
            pass
        else:
            files_detected += 1
            selectedFiles.append(file)


    if files_detected >= 1:
        UserWish = input(f"A total of {files_detected} were detected to change. Do you wish to create a new directory? [y/n]")
        if UserWish == "y" or "Y":
            while True: 
                try:
                    saved_img_folder = input("Enter new directory for the images to be saved: ")
                    os.makedirs(saved_img_folder)
                    break
                except FileExistsError:
                    print("The file directory already exists")
                    continue

            files_converted += 1
            saving_images(selectedFiles=selectedFiles , saving_directory=saved_img_folder)
            # save_log(file, files_detected, files_converted, files_skipped, files_corrupted, convertedFile_named)

        if UserWish == "n" or "N":
            print("User aborted")
            # saved_img_folder = f"{UserInput}/ConvertedFiles"
            # files_converted += 1
            # saving_images(target_file=f"{UserInput}\\{file}", fileName=file , saving_directory=saved_img_folder)
            # save_log(file, files_detected, files_converted, files_skipped, files_corrupted, convertedFile_named)

    else:
        print("No files of .jpg were detected")



# if files_converted == 0:
#     print(
#         f"No files were converted. All present {files_detected} files are not .jpg"
#         " format"
#     )
#     time.sleep(3)
# elif files_corrupted == 0 and files_converted == 0:
#     print(
#         f"Script found {files_corrupted}.jpg files that are corrupted. No files"
#         " were converted."
#     )
# else:
#     print(f"Program completed converting {files_converted} Files.\nExiting now...")
#     time.sleep(2)



script_Runtime()