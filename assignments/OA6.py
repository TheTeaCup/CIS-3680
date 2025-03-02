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
    validValues = []
    minValue = 0
    maxValue = 0
    meanValue = 0 

    for line in file:
        if line.startswith('-'):
            missingValues = missingValues + 1
        else:
            validValues.append(float(line))

    minValue = min(validValues)
    maxValue = max(validValues)
    meanValue = statistics.mean(validValues)

    print('Missing Values:', missingValues)
    print('Valid Values:', len(validValues))
    print('Min:', minValue)
    print('Max:', maxValue)
    print(f'Mean: {meanValue:.4f}')

if __name__ == "__main__":
    main()