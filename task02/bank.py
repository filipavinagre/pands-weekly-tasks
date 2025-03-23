# bank.py
# This program prints out two money amounts in cents and then add them together in euros.
# Author: Filipa Vinagre

amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))
print (f"The amount1 is {amount1} cents and amount2 is {amount2} cents")
# The code here will prompt the user to enter the two amounts in cents and once this is answered by the user it will print the amount1 and amount2 (in cents). This is done as integer to avoid rounding errors.

total_cents = amount1 + amount2
total_euros = total_cents/100
print (f"The sum of these is €{total_euros:.2f}")
# The first line of the code will add the two amounts in cents, and the second line will convert them in euros, ensuring a decimal point between euro. The value to be printed will be the total amount in euros. Reference to do this task found here:https://www.w3schools.com/python/python_string_formatting.asp