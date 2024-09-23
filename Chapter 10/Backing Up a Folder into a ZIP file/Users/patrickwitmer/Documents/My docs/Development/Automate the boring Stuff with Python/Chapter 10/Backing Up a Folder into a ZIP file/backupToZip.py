#! python3 
# backupToZip.py - Copys an entire folder and its contents into a ZIP file whose filename increments.

import zipfile, os

def backuptoZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # makes sure the path is absolute

    # Figure out the filename this code should use based on what files already exist
    number = 1
    while True: 
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create the ZIP file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entore folder tree and compress files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
        
    backupZip.close()
    print('Backup complete.')


backuptoZip('/Users/patrickwitmer/Documents/My docs/Development/Automate the boring Stuff with Python/Chapter 10/')
