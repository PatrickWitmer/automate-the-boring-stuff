import os, shutil, re

# regex to find zeroes
zeroPattern = re.compile(r'0+')

for filename in os.listdir('.'):
  # Remove zeroes from the filename
  zeroFilename = zeroPattern.sub('', filename)

  # Rename the files
  print('Renaming "%s" to "%s"...' % (filename, filename))
  # shutil.move(filename, filename) # Uncomment after testing