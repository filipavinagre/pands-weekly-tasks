# Weekly Task 04 - collatz.py
# Autor: Filipa Vinagre

# Project Description:
This program "collatz.py", asks the user to input any positive integer and outputs the successive values of the following calculation. 

At each step calculate the next value by taking the current value and:
    - if it is even, divide it by two;
    - if it is odd, multiply it by three and add one.

The program ends if the current value is one. 

## How will it look like?  
    $ python collatz.py 
    Please enter a positive integer: 10 
    10 5 16 8 4 2 1

# Installation
Python is needed to run this project. 
You can dowload it from the official site: (https://www.python.org/downloads/)

## How to run?
'''bash
python collatz.py

# Outlined steps
1. The programp prompts the user to enter a positive integer.
2. If the user enters a number greater than zero the program will print out a Collatz Sequence (3n + 1).
3. A Collatz Conjucture allows to convert any positive integer into 1 by repeating two arithmetic operations:
    - If the current value is even, divide it by two, 
    - If the current value is odd, multiply it by three and add one
    - The sequence finishes when the current value is one.
4. If the user enters a number less than zero the program will print an error message indicating the user the number should be greater than zero.

# References

[Exploring the Collatz Conjucture with Python](https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233)
    
[How to generate the Collatz sequence in Python](https://how.dev/answers/how-to-generate-the-collatz-sequence-in-python)

[Collatz Sequence in Python: Iterative VS Recursive](https://www.youtube.com/watch?v=jtjr_g8SJd4)

[Append() Operator](https://realpython.com/python-append/)