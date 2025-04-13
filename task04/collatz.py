# collatz.py
# This program prompts the user to input any positive integer and outputs the successive values through Collatz Conjuncture - At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one until the current value is one.
# Author: Filipa Vinagre

# Prompt the user to input any positive integer.
number = int(input("Enter any positive number: "))

# While loop & If, Else Stamentents used below to ensure the the number entered by the user is greater than zero. If not, the program will print an error message and prompt user to enter a positive number.

while True:
    
    if number > 0:
        n = number
        break
    else:
        print ("ERROR: Please enter a positive number.")
        number = int(input("Enter any positive number: "))

# Def Collatz Sequence Function.

def collatz_sequence(n):
    sequence = [n]

# While loop & If, Else Stamentents used below to perform two arithmetic operations to convert any positive integer into one and retun the sequence.

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        sequence.append (n)
    return sequence

print (collatz_sequence(n))


# Breakdown on function above: 
# Defining collatz function
# until when n is not equal to 1, it means, the sequence keeps running until it reaches 1: 
# If number is even (%) divide by two until reaches 0 // to avoid float numbers
# If not multiply by 3 and add 1
# Sequence append n - to apply this to the sequence, so program can run many times it needs until reaches 1