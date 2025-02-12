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

def main():
    # Get input for Sign Material, Text, and Letter Color
    material = input("Enter sign material (Oak or Pine): ")
    signText = input("Enter sign text: ")
    letterColor = input("Enter letter color (Black, White, or Gold): ")

     # Const price
    PRICE = 30

    # determine material cost
    if material == "Oak":
        PRICE += 15
    elif material == "Pine":
        PRICE = PRICE

    # determine letter cost
    if len(signText) > 6:
        PRICE += (len(signText) - 6) * 3

    # determine letter color cost
    if letterColor == "Gold":
        PRICE +=12

    # output
    print(f"The total cost of the sign is: ${PRICE}")

main()