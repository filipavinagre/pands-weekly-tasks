# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Filipa Vinagre

# Import datetime
from datetime import datetime

# Defining 
dt = datetime.now()

wd = dt.weekday()

if wd < 4:
    print ("Yes, unfortunately today is a week day!")
elif wd == 4:
    print ("The weekend is near; Happy Friday!")
else:
    print ("Yay, it's the weekend!! Enjoy it!")