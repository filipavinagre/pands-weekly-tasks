# Weekly Task 05 - weekday.py
# Autor: Filipa Vinagre

# Project Description:
This program "weekday.py" outputs whether or not today is a weekday without user's input. 
If the program is open on a weekday the program automatically prints a message indicating it is a weekday and if the program is run on a weekend the program automatically prints a message indicating it is weekend.

## How will it look like?  
e.g: Program runs on a Wednesday:
    $ python weekday.py 
    Yes, unfortunately today is a weekday. 
    
e.g. Program runs on a Saturday: 
    $ python weekday.py 
    Yay, it's the weekend!! Enjoy it!

# Installation
Python is needed to run this project. 
You can dowload it from the official site: (https://www.python.org/downloads/)

Additionally you will need to import the datetime module into python.
    '''python from datetime import datetime'''

## How to run?
'''bash
python weekday.py'''

# Outlined steps
1. Once the program runs a message will be printed indicating is it is a weekday or weekend day:
    - If the program is running between Monday and Thursday the program prints out "Yes, unfortunately today is a week day!"
    - If the program is running on a Friday the program prints out "The weekend is near; Happy Friday!"
    - If the program is running on a Saturday or Sunday the program prints out "Yay, it's the weekend!! Enjoy it!"

# References

[Weekday Function](https://pynative.com/python-get-the-day-of-week/)