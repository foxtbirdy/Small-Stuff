# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-12-14 01:36:40
# @Last Modified by:   Climax
# @Last Modified time: 2021-12-19 22:44:54

import PyPDF2 
import sys
import os 
import time

target_directory = os.listdir(os.path.dirname(sys.argv[0])) # select script files
target_files = []



# validate all the files and find exceptional
for file in target_directory:
	if file == os.path.basename(sys.argv[0]): pass;
	elif os.path.splitext(file)[1] != ".pdf" : pass;
	else: target_files.append(file)

def pdf_combiner(pdf_list, super_file_name):
	merger = PyPDF2.PdfFileMerger()
	for file in pdf_list:
		merger.append(file)
	merger.write(super_file_name)



# confirm the user the files that are about to be edited
def main(pdf_list):
	while True:
		if len(pdf_list) < 1:
			print("No PDF files in this folder were to merge.")
			time.sleep(4)
			break
		merged_file_name = f'{input("Enter merged file name: ")}.pdf'
		user_input = input(f"A total of {len(pdf_list)} will be merged in '{merged_file_name}'. Do you wish to merge them(y/n)? > ")
		if user_input == "y":
			pdf_combiner(target_files, merged_file_name)
			break
		elif user_input == "n":
			break
		else:
			print("[INVALID COMMAND]")  


main(target_files)


