"""
OA #6 - Hunter Wilson

Create a program to process the file data.txt
Find the following pieces of information about the file:

    Number of missing values (-1)
    Number of valid values
    Min
    Max
    Mean

Output your result to the console.
Hint: import and use the statistics module.
"""
import statistics

def main():
    fileName = input("Enter the file name: ")
    file = open(fileName, 'r')

    missingValues = 0
    validValues = 0
    minValues = 0
    maxValues = 0
    meanValues = 0 

    for line in file:
        print(line)

        if line.startswith('-'):
            missingValues = missingValues + 1

    print('Missing Values', missingValues)

main()