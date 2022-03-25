# .rtf to .md File Converter

## Purpose
This script takes .rtf files, converts them to Python strings,
exports the strings as .txt files,
and changes the filetype from .txt to .md

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
![Stack Overflow](https://stackoverflow.com/questions/16736080/change-the-file-extension-for-files-in-a-txt_folder)
