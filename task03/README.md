# Weekly Task 03 - accounts.py
# Autor: Filipa Vinagre

# Project Description:
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs). 

This program "accounts.py" reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs). 
    Extra: As an extra the program was modified in the second part of the code to deal with account numbers of any length.

## How will it look like?  
    $ python accounts.py 
        Please enter an 10 digit account number: 1234567890 
        XXXXXX7890 

# Installation
Python is needed to run this project. 
You can dowload it from the official site: (https://www.python.org/downloads/)

## How to run?
'''bash
python collatz.py

# Outlined steps
1. Prompt the user to enter 10 character account number.
2. If the account number is 10 digits, the program prints out the account number with only the last 4 digits showing and the first 6 digits replaced with Xs.
3. If the account number is not 10 digits, the program prints out an error mesage indicating account number must be 10 digits.

Extra step
5. Prompt the user to enter an account number.
6. The program reads in the account number, regardless of it´s lenght and outputs the account number with only the last 4 digits showing.
7. The program only works if the account number is formed with only digits, no other characters.

# Extra Step Assumptions
For the extra part of the task, I modified the program as required to deal with account numbers of any lenght ensuring that:
    - A bank account number must consist in only numbers, no letters or symbols.
    - The last 4 digits of the bank account will always be displayed, while any previous digits will be replaced with Xs.

To complete this I followed the same thought process of the first part of the program and used the If, Else function, along with other conditions:
    - Started the program prompting the user to enter their bank account number.
    - Used "If not" Statement to ensure the value entered is only digits, through .isdigit() function. 
        - If the value entered doesn´t meet the criteria, an error message is printed out indicating the user the bank account must only contain numbers.
    - Used "Else" Statement to print out the bank account number as per required in the task. First defined the last 4 digits through the slice function, then defined how the protected number should look like - replacing all numbers with Xs, except the last 4, then concatenated the last 4 digit.
    - The program then prints out the protected number.

# References

If;Else Function:
    Class Material 4 
    [Python Conditions w3](https://www.w3schools.com/python/python_conditions.asp)
    [If, Elif, Else Video](https://www.youtube.com/watch?v=FvMPfrgGeKs)  

While True:
    Class Material 4 
    [Python While Loops w3](https://www.w3schools.com/python/python_while_loops.asp)
    [While Loops Video](https://www.youtube.com/watch?v=rRTjPnVooxE)
    [Python While True Loop Video](https://youtu.be/phDGzshEzRQ?feature=shared )

IsDigit() Function:
    Prompt AI to provide me at least 3 the options available in python to ensure a value entered is only digits, no letters or symbols, from the response did further reading.
    [isdigit() w3](https://www.w3schools.com/python/ref_string_isdigit.asp)
    [isdigit() programiz](https://www.programiz.com/python-programming/methods/string/isdigit)

Lenght Function:
    Class Material 3
    [Python string lenght](https://www.geeksforgeeks.org/python-string-length-len/?ref=next_article_top)
    [Python len()](https://docs.vultr.com/python/built-in/len)

Slicing Function:
    Prompt AI how to I return a value in python modified, including some information from a value and modify another, from the response did further reading. 
    [Python List Slicing](https://www.geeksforgeeks.org/python-list-slicing/)
    [Python Slice Function w3](https://www.w3schools.com/python/ref_func_slice.asp)