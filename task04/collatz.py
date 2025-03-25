# collatz.py
# This program prompts the user to input any positive integer and outputs the successive values.
# Author: Filipa Vinagre

# Prompt the user to input any positive integer
n = int(input("Enter any positive number: "))

# Def Collatz Sequence Function
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one until the current value is one.
def collatz_sequence(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        sequence.append (n)
    return sequence

print (collatz_sequence(n))


# References: Understand Collatz Sequence in Python https://www.youtube.com/watch?v=jtjr_g8SJd4 & https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233 & https://how.dev/answers/how-to-generate-the-collatz-sequence-in-python
# Reference: https://how.dev/answers/how-to-generate-the-collatz-sequence-in-python
# Breakdown on function above: 
## Defining collatz function
## until when n is not equal to 1, it means, the sequence keeps running until it reaches 1: 
## If number is even (%) divide by two until reaches 0 // to avoid float numbers
## If not multiply by 3 and add 1
## Sequence append n - to apply this to the sequence, so program can run many times it needs until reaches 1
## 
## 