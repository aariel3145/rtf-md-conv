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

# parse .rtf folder
for filename in os.listdir(info['in_folder']):
    base = filename[0:-len(info['oldType'])]

    # convert from oldType to midType
    rtf_txt(info, base)

    # convert from midType to newType
    txt_md(info, base)
    

