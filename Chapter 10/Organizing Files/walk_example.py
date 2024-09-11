import os
from pathlib import Path

path = Path.home() / 'Documents' / 'My docs' / 'Development' / 'Automate the boring Stuff with Python' / 'Chapter 10' / 'Organizing Files' / 'some_folder'

for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
