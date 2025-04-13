# bank.py
# This program prints out two money amounts in cents and then add them together in euros.
# Author: Filipa Vinagre

# Prompt the user to enter the two amounts in cents. This is done as integer to avoid rounding errors.

amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))

# The first line of the code will add the two amounts in cents, and the second line will convert them in euros. The value to be printed will be the total amount in euros ensuring a decimal point between euro through f-string ".2f modifier".

total_cents = amount1 + amount2
total_euros = total_cents/100
print (f"The sum of these is €{total_euros:.2f}")