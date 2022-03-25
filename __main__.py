import os
import sys

from functions import *

info = {
    'in_folder' : "D:/Dropbox/Creative Projects/Coding/rtf-md-conv/rtf_infile",
    'mid_folder' : "D:/Dropbox/Creative Projects/Coding/rtf-md-conv/txt_md_outfile",
    'out_folder' : "D:/Dropbox/Creative Projects/Coding/rtf-md-conv/txt_md_outfile",
    'oldType' : '.rtf',
    'midType' : '.txt',
    'newType' : '.md'
}

success = 0
failure = 0

# parse .rtf folder
for filename in os.listdir(info['in_folder']):
    base = filename[0:-len(info['oldType'])]

    # convert from oldType to midType
    error = rtf_txt(info, base)
    # convert from midType to newType
    error = txt_md(info, base)

    if error == True:
        failure += 1
    else:
        success += 1

print(f"\n\t{failure} files failed | {success} files converted\n")
    

