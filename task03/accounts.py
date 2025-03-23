# accounts.py
# This program reads in a 10 character account number and outputs the account numer with only the last 4 digits showing and the first 6 digits replaced with Xs.
# Author: Filipa Vinagre

#Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

# Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

#$ python accounts.py
# Please enter an 10 digit account number: 1234567890
# XXXXXX7890

# Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

# Prompt user for account number
account_number = input("Please enter an 10 digit account number: ")

# Condition if; else
if len(account_number) == 10:
    protected_number = ("X" * 6 + account_number [6:10])
    print (protected_number)
else:
    print ("error")



# references: 
# https://www.w3schools.com/python/python_conditions.asp if, else condition
# https://www.geeksforgeeks.org/python-string-length-len/?ref=next_article_top lenght function
