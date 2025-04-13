# Weekly Task 07 - es.py
# Autor: Filipa Vinagre

# Project Description:
This program "es.py" reads in a text file and outputs the number of e's it contains, dealing with errors such as filename that does not exist, or is not a text file.
The program takes the filename from an argument on the command line.   
The assumptions made are documented below. 

## How will it look like?  
    $ python es.py 
    peter-piper.txt 
    42

# Installation
Python is needed to run this project. 
You can dowload it from the official site: (https://www.python.org/downloads/)

Additionally you will need to import the sys and os modules into python.
    '''
    python 
    import sys
    '''
    
    '''
    python 
    import os
    '''

## How to run?
'''
bash
python es.py peter-piper.txt
'''

# Outlined steps
1. Once the program is running the number of E's within the text file will be counted and printed out.

# Considerations
1. The filename must be taken from an argument on command line. 
1. Created a text file named peter-piper

Approach taken
Tried to break down the task into small pieces
Created a text file
Looked what was argument on the command line and the kinds of approaches to take
sys to import as it was easier for begginners
created the code to open the text file and output the ammmount of E's in the file 
took the assumption of counting case sensitive, reading all file
From the code base looked at how could additional features could be included - error messages
Import OS to check if file exists


# References

Class Material 7

[Command line and environment](https://docs.python.org/3/using/cmdline.html)

[Command Line Arguments video](https://www.youtube.com/watch?v=ZQ9JO0e9468)

[Handling Text Files in Python](https://www.codecademy.com/article/handling-text-files-in-python)

[Python Program to Count the Number of Occurrence of a Character in String](https://docs.vultr.com/python/examples/count-the-number-of-occurrence-of-a-character-in-string)

[Count() Function w3](https://www.w3schools.com/python/ref_string_count.asp)

[Lower () String w3](https://www.w3schools.com/python/ref_string_lower.asp)
