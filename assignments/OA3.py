"""
OA #3 - Hunter Wilson

Signs-R-Us makes personalized signs. 
They would like an application to compute the price of a sign based on the following factors:
    The minimum charge for a sign is $30.
    If the sign is made of Oak, add $15. No charge is added for pine.
    The first six letters or numbers are included in the minimum charge. 
    There is a $3 charge for each additional letter.
    Black or white characters are included in the minimum charge. 
    There is an additional $12 charge for gold-leaf lettering.
Create a program to calculate the price of a sign.
"""

# Const price
PRICE = 30

# Get input for Sign Material, Text, and Letter Color
material = input("Enter sign material (Oak or Pine): ")
signText = input("Enter sign text: ")
letterColor = input("Enter letter color (Black, White, or Gold): ")

# determine material cost
if material == "Oak":
    PRICE += 15
elif material == "Pine":
    PRICE = PRICE
else:
    print("Invaild sign material")

# determine letter cost



# determine letter color cost



# output
print(f"The total cost of the sign is: ${PRICE}")