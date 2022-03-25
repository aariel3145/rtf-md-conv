### 
# convert .rtf to .txt
# forked from https://github.com/joshy/striprtf
###

###
# Change File Extneion for Files in a Folder
# from https://stackoverflow.com/questions/16736080/change-the-file-extension-for-files-in-a-folder
###

import os, sys
folder = 'D:\Dropbox\Creative Projects\Coding\rtf-md-conv\rtf_infile'
oldType = '.txt'
newType = '.md'

for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename) : continue
    oldbase = os.path.splittext(filename)
    newname = infilename.replace(oldType, newType)
    output.os.rename(infilename, newname)
