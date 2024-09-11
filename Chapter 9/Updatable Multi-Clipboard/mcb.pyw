#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.

# Created in 2024 Patrick Witmer via the book Automate the Boring Stuff with Python.

# Usage:  mcb.pyw save <keyword> - Saves clipboard to keyword.
#         mcb.pyw <keyword> - Loads clipboard from clipboard.
#         mcb.pyw list - Lists all keywords clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save Clipbard to content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
  # List keywords and load content.
  if sys.argv[1].lower() == 'list':
     pyperclip.copy(str(mcbShelf.keys()))
  elif sys.argv[1] in mcbShelf:
     pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()