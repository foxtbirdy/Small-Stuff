# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-12-14 01:36:40
# @Last Modified by:   Climax
# @Last Modified time: 2021-12-14 02:02:50

import PyPDF2 
import sys
import os 


target_files = os.listdir(os.path.dirname(sys.argv[0])) # select script files


def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for file in target_files:
		if file == os.path.basename(sys.argv[0]): pass;
		elif os.path.splitext(file)[1] != ".pdf" : pass;
		else: merger.append(file)

	merger.write('super.pdf')


pdf_combiner(target_files)









