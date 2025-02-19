"""
PA #4 - Hunter Wilson
A biologist needs a program to predict population growth. The inputs
are:
1) The initial number of organisms, as an int
2) The rate of growth (a real number greater than 1), as a float
3) The number of hours it takes to achieve this rate, as an int
4) The number of hours during which the population grows, as an int

Write a program that takes these inputs and displays a prediction of the
total population.
"""

def calculateTotalPopulation(initialOrganisms, rateOfGrowth, hoursForGrowth, totalHours):
    return initialOrganisms * (rateOfGrowth ** (totalHours // hoursForGrowth))

def main():
    # Collect initial organisms as a int
    initialOrganisms = int(input("Enter the inital number of organisms: "))

    # Do a while loop to allow the user to input the rate of growth as a float as long as its greater than 1
    while True:
        rateOfGrowth = float(input("Enter the rate of growth (a real number > 1): "))
        if rateOfGrowth > 1:
            break
        print("Error: The rate of growth must be greater than 1. Please enter again.")

    # Collect the number of hours needed to achieve the rate of growth
    hoursForGrowth = int(input("Enter the number of hours to achieve the rate of growth: "))

    # Collect the total hours of growth
    totalHours = int(input("Enter the total hours of growth: "))
    
    # calculate the organisms with the rate of growth
    totalPopulation = calculateTotalPopulation(initialOrganisms, rateOfGrowth, hoursForGrowth, totalHours)

    print(f"The total population is {int(totalPopulation)}")

main()