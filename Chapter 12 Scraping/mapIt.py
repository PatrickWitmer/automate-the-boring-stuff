#! python3

# mapIt.py - Launches a map in the browser using an address from the command line of clipboard.

import sys

import webbrowswer

if len(sys.argv) > 1:
    # Get address from the command line.
    address = sys.argv[1:]

# TODO: Get the address from the clipboard
