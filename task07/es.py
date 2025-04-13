# es.py
# This program reads in a text file and outputs the number of e's it contains.
# Author: Filipa Vinagre

# Import sys - to access command line arguments.
import sys

# Import OS - to look if a file exists.
import os

# Command line arguments

filename = sys.argv[1]

# Check is not a text file
if not filename.endswith(".txt"):
     print ("ERROR: The file must be a .txt file.")

# Check if file exists
if not os.path.exists (filename):
     print (f"ERROR: The file '{filename}' does not exist.")


# Read file
with open (filename, 'tr') as f:
    data = f.read()

# Count E's
    count = data.lower().count("e")
    print (count)
