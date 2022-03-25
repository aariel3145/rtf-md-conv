# .rtf to .md File Converter

## Purpose
This script takes .rtf files, converts them to Python strings,
exports the strings as .txt files,
and changes the filetype from .txt to .md

## How to Use
```python
info = {
    'in_folder' : "[location of incoming files]",
    'mid_folder': "[location of intermediary files]",
    'out_folder': "[location of final files (may be same as intermediary)]",
    'oldType'   : "[incoming file extension, i.e. '.rtf']",
    'midType'   : "[intermediary file extension, i.e. '.txt']",
    'newType'   : "[final file extension, i.e. '.md']"
}
```

## Intended Use
To convert rich text files, exported from a previous journaling program,
to markdown for a current journaling program.
Intended to be modular so that different starting file types are possible
with the addition of various functions.
For example, use a .docx-to-.txt script and then this script's
.txt-to-.md features.

## Based On:
### striprtf
![Build status](https://github.com/joshy/striprtf/workflows/striprtf%20build/badge.svg)
### Change File Extension for Files in a Folder
[Stack Overflow](https://stackoverflow.com/questions/16736080/change-the-file-extension-for-files-in-a-txt_folder)
