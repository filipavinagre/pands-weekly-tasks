# pands-weekly-tasks
# Autor: Filipa Vinagre

# Weekly Tasks 02 - bank.py
When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
Write a program called bank.py 
The program should:
Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45
Advice: There is a bit in this, break it down into smaller parts, for example read in an integer first, and print it back out again, then do some arithmetic to it and print, then read in a second one and add the two, and only then look at the formatting of the answer. of course there are many ways of doing this.

# Weekly task 03 - accounts.py
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
Extra:
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

# Weekly Tasks 04 - collatz.py
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.
Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).
Example of it running:
$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1

# Weekly Task 05 - weekday.py
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
You will need to search the web to find how you work out what day it is.
An example of running this program on a Thursday is given below.
$ python weekday.py
Yes, unfortunately today is a weekday.
An example of running it on a Saturday is as follows:
$ python weekday.py
It is the weekend, yay!
There is no user input.

# Weekly Task 06 - 
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 
This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

# Weekly Task 07 - 
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.
$ python es.py moby-dick.txt
116960

# Weekly Task 08 - plottask.py
Write a program called plottask.py that displays:
a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).
Please put a copy of the image of the plot (.png file) into the repository