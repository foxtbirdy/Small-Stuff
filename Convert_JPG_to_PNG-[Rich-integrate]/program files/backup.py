import os
import sys
import PIL
from PIL import Image
import time

"""
backup code. there are a couple of errors with the print so be careful. covert logic works.
"""




UserInput = input("Enter your directory here: ")
target_directory_listdir = os.listdir(UserInput)  # address to script's directory
saved_img_folder = f"{UserInput}/ConvertedFiles" # if the user doesn't want to create a new directory.


def saving_images(selectedFiles, saving_directory):
    for file in selectedFiles:
        print("File converting => ", file , saving_directory)
        img = Image.open(f"{UserInput}/{file}")
        img.save(f"{saving_directory}/{file}.png")


# def save_log(file, files_detected, files_converted, files_skipped, files_corrupted, convertedFile_named, saved_img_folder):
#     with open(f"{saved_img_folder}/Script Log.txt", mode="w") as log_file:
#         log_file.write(f"Items Detected - {str(files_detected)} \n")
#         log_file.write(f"Images Converted - {str(files_converted)} \n")
#         log_file.write(f"Images Skipped - {str(files_skipped)} \n")
#         log_file.write(f"Images Found Corrupted - {str(files_corrupted)} \n\n")
#         log_file.close()

#     convertedFile_named.append(file)
#     with open(f"{saved_img_folder}\\Script Log.txt", mode="a") as log_file:
#         for file_count in convertedFile_named:
#             log_file.write(f"{file_count} \n")


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


    for i in selectedFiles: print(i)






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
        elif UserWish == "n" or "N":
            print("User aborted")
    else:
        print("No files of .jpg were detected")


script_Runtime()