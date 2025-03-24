# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Filipa Vinagre

# Import datetime
from datetime import datetime

dt = datetime.now()

wd = dt.weekday()

if wd < 5:
    print ("Yes, unfortunately today is a week day!")
else:
    print ("yay, it's the weekend!")



# Reference: Weekday function used from https://pynative.com/python-get-the-day-of-week/
