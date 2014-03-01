#!/usr/bin/Python3
#
#   WATHCITF script : What are the hexa colors in this file ?
#
#   Romain (BucOder) SOMMERARD
#   http://www.bucoder.com
#   Distributed under the GPL version 3 licence
#
#   Search all hexa color in the css file
#
#   Usage:  Replace the PATH_FILE by the path of
#           your file name and run this script.
#
#   Syntax: 	# Python3 wathcitf
#		
#		OR      
#
#		# Python wathcitf
#
#		OR
#
#		# chmod +x wathcitf
#               # ./wathcitf
#

import re

# The path of css file
PATH_FILE = ''

if PATH_FILE == '':
    print('Error: PATH_FILE empty')
    exit(1)

colors = set()

expression = r'(#[0-9a-fA-F]{3,6})'

with open(PATH_FILE, 'r') as file:
    for line in file:
        color = re.match(expression, line)
        if color:
            colors.add(color.group(0))
            

for color in colors:
    print(color)
