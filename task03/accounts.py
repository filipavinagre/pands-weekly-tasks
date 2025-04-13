# accounts.py
# This program reads in a 10 character account number and outputs the account numer with only the last 4 digits showing and the first 6 digits replaced with Xs.
# Author: Filipa Vinagre

# PROGRAM 1: Reads in a 10 digit account number and outputs the account number with only the last 4 digits showing.

# Prompt user for 10 digit account number.

account_number = input("Please enter your account number: ")

# While loop & If, Else Stamentents used below to ensure the program only stops when user enters 10 digits. The program will print the account number with only the last 4 digits showing. If account number is not 10 digit the program will print an error message.

while True:
    
    if len(account_number) == 10 and account_number .isdigit():
        protected_number = ("X" * 6 + account_number [6:10])
        print (protected_number)
        break
    else:
        print ("ERROR: Account number must be 10 digits.")
        account_number = input("Please enter your account number: ")

# PROGRAM 2: Reads in an account number, regardless of it´s lenght and outputs the account number with only the last 4 digits showing.

# Prompt user for account number.

account_number1 = input("Please enter your account number: ")

# If Not Condition used to only accept digits as an account number, if other type of caracters are entered the program will print an error message; else function determines last 4 digit to be shown and any numbers before these to replaced with Xs, which will then be printed out.

if not account_number1 .isdigit():
     print ("ERROR: Account number must only contain digits.")      
else:
    last_four = account_number1[-4:]
    protected_number2 = "X" * (len(account_number1) - 4) + last_four
    print (protected_number2)