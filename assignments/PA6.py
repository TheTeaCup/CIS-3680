"""
PA #6 - Hunter Wilson

The Payroll Department keeps a list of employee information for each pay period in a text file. The format of each line of the file is the following:

<last name> <hourly wage> <hours worked>

Write a program that inputs a filename from the user and prints to the terminal a report of the wages paid to the employees for the given period. The report should be in tabular format with the appropriate header. Each line should contain an employee's name, the hours worked and the wages paid for that period.

Example Run:

Enter the file name: data.txt
Name            Hours   Total Pay
Hodges             34      357.00
Corley             22      159.50
Hunsinger           5      503.50
"""

def main():
    fileName = input("Enter the file name: ")
    file = open(fileName, 'r')

    print("Name\t\tHours\tTotal Pay")
    for line in file:
        words = line.split()
        name = words[0]
        wage = words[1]
        hours = words[2]
        pay = float(wage) * float(hours)

        if len(name) >= 8:
            print(name + "\t" + str(hours) + "\t" + f"{pay:.2f}")
        else:
            print(name + "\t\t" + str(hours) + "\t" + f"{pay:.2f}")

main()