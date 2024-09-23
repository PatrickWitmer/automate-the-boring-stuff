import os, shutil

# Loop over files in the directory
for filename in os.listdir('.'):

  # Add the prefix to the filename
  prefixFilename = '666_' + filename
  

  # Rename the files
  print('Renaming "%s" to "%s"...' % (filename, prefixFilename))
  # shutil.move(filename, prefixFilename) # Uncomment after testing