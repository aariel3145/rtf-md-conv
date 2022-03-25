import os
import sys

### 
# convert .rtf to .txt
# forked from https://github.com/joshy/striprtf
###
def rtf_txt(info, base):  
    
    from striprtf.striprtf import rtf_to_text
    
    # figure out infile name
    infilename = (info['in_folder'] + "/" + base + info['oldType'])

    # open file to read
    try:
        rtf_file = open(infilename, 'r')
    except:
        print("could not open " + infilename)
        return True
    # read into string
    rtf_string = rtf_file.read()
    # close input file
    rtf_file.close()

    # convert to middle type
    txt_string = rtf_to_text(rtf_string)

    # figure out txt outfile name
    txt_filename = (info['mid_folder'] + "/" + base + info['midType'])

    # save string as .txt file
    try:
        txt_file = open(txt_filename, 'w')
    except:
        print("could not open " + txt_filename)
        return True
    txt_file.write(txt_string)
    txt_file.close()

###
# Change File Extneion for Files in a Folder
# from https://stackoverflow.com/questions/16736080/change-the-file-extension-for-files-in-a-folder
###
def txt_md(info, base):

    txt_filename = info['mid_folder'] + "/" + base + info['midType']
    out_filename = info['out_folder'] + "/" + base + info['newType']
    # check if we are overwriting or saving again
    if info['mid_folder'] != info['out_folder']:
        # open intermediate file, copy text
        try:
            txt_file = open(txt_filename, 'r')
        except:
            print("could not open " + txt_filename)
            return True
        txt_string = txt_file.read()
        txt_file.close()

        # open output file, paste text
        try:
            out_file = open(out_filename, 'w')
        except:
            print("could not open" + out_filename)
            return True
        out_file.write(txt_string)
        out_file.close()
    else:
        # change output file from .txt to .md
        newname = txt_filename.replace(info['midType'], info['newType'])
        try:
            os.rename(txt_filename, newname)
        except FileExistsError:
            print(newname + " already exists")
            return True

def rename_base(info, base):

    out_filename = info['out_folder'] + "/" + base + info['newType']
    # rearrange to yyyy-mm-dd
    newbase = "20" + base[4:6] + "-" + base[0:2] + "-" + base[2:4]
    new_filename = info['out_folder'] + "/" + newbase + info['newType']

    os.rename(out_filename, new_filename)
