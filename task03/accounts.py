# accounts.py
# This program reads in a 10 character account number and outputs the account numer with only the last 4 digits showing and the first 6 digits replaced with Xs.
# Author: Filipa Vinagre

# Program 1: Reads in a 10 charater account number and outputs the account number with only the last 4 digits showing.

# Prompt user for 10 digit account number
account_number = input("Please enter an 10 digit account number: ")

# Outputs the 10 character account number with only the last 4 digits showing.
if len(account_number) == 10:
    protected_number = ("X" * 6 + account_number [6:10])
    print (protected_number)
else:
    print ("ERROR: Account number must be 10 digits.")

# Program 2: Reads in an account number, regardless of it´s lenght and outputs the account number with only the last 4 digits showing.

# Prompt user for account number
account_number1 = input("Please enter an 10 digit account number: ")

# Condition if; else

if len(account_number1) == 10:
    protected_number1 = ("X" * 6 + account_number [6:10])
    print (protected_number1)
else:
    last_four = account_number1[-4:]
    protected_number2 = "X" * (len(account_number1) - 4) + last_four
    print (protected_number2)

## References:  
### For the If;Else Function used Class Material 4 + https://www.w3schools.com/python/python_conditions.asp 
### For the Lenght Function, used Class Material 3 where this was briefly mentioned and did further reading on https://www.geeksforgeeks.org/python-string-length-len/?ref=next_article_top to better understand it.
### For the Slicing Function, used AI (ChatGPT) how to tackle only the last 4 digits and did further reading on https://www.geeksforgeeks.org/python-list-slicing/