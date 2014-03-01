#!/usr/bin/Python3
#
#   Wathcitf script : What are the hexa colors in this file ?
#
#   Romain (BucOder) SOMMERARD
#   http://www.bucoder.com
#   Distributed under the GPL version 3 licence.
#
#   Search all hexa colors in the css file.
#   Script for Linux system.
#
#   Usage:  Replace the PATH_FILE by the path of
#           your file name and run this script.
#
#   Syntax: 	# Python3 wathcitf
#		
#		OR      
#
#               If python 3 is the only version of python in your computer.
#		# Python wathcitf
#
#		OR
#
#               You can run the script like application.
#		# chmod +x wathcitf
#               # ./wathcitf
#

import re
import os


# The path of folder where is the file.
FOLDER_PATH = ''

# The css file name.
FILE_NAME = ''


if FOLDER_PATH == '':
    print('Error: FOLDER_PATH empty')
    exit(1)

if FILE_NAME == '':
    print('Error: FILE_NAME empty')
    exit(0)

colors = set()

expression = r'(.*)(#[0-9a-fA-F]{3,6})(.*)'

os.system('cd ' + FOLDER_PATH)

try:
    with open(FILE_NAME, 'r') as file:
        for line in file:
            color = re.match(expression, line)
            if color:
                colors.add(color.group(2))
except FileNotFoundError:
    print('Error: File not found (',PATH_FILE,')',sep='')
    exit(1)            

for color in colors:
    print(color)
