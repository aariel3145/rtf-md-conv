import os
import sys
from striprtf.striprtf import rtf_to_text

### 
# convert .rtf to .txt
# forked from https://github.com/joshy/striprtf
###

###
# Change File Extneion for Files in a Folder
# from https://stackoverflow.com/questions/16736080/change-the-file-extension-for-files-in-a-txt_folder
###

rtf_folder = "D:/Dropbox/Creative Projects/Coding/rtf-md-conv/rtf_infile"
txt_folder = "D:/Dropbox/Creative Projects/Coding/rtf-md-conv/txt_md_outfile"
oldType = '.rtf'
midType = '.txt'
newType = '.md'

# parse .rtf folder
for filename in os.listdir(rtf_folder):
    # figure out rtf infile name
    infilename = os.path.join(rtf_folder, filename)
    if not os.path.isfile(infilename) : continue

    # open .rtf file to read
    rtf_file = open(infilename, 'r')
    # read into string
    rtf_string = rtf_file.read()
    # close .rtf file
    rtf_file.close()

    # convert rtf to text
    txt_string = rtf_to_text(rtf_string)

    # figure out txt outfile name
    txtfilename = (txt_folder + "/" + filename[0:len(filename)-4] + midType)

    # save string as .txt file
    txt_file = open(txtfilename, 'w')
    txt_file.write(txt_string)
    txt_file.close()

    # rename from .txt to .md
    oldbase = os.path.splitext(filename)
    newname = txtfilename.replace(midType, newType)
    output = os.rename(txtfilename, newname)
