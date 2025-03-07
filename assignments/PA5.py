"""
PA #5 - Hunter Wilson

A list is sorted in ascending order if it is empty 
or each item except the last one is less than or equal to its successor. 
Define a function called is_sorted that expects a list as an argument and
returns True if the list is sorted, or returns False otherwise. 
Include a brief main program to demonstrate the function.
(Hint: For a list of length 2 or greater, 
loop through the list and compare pairs of items, 
from left to right, and return False if the first item in a pair is greater.)
"""

def is_sorted(list):
    # if the list is empty or has 1 item then its 'sorted'
    if len(list) <= 1:
        return True
    
    # loop through the list
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False # if any pair is out of order then its not 'sorted'
        
    # otherwise the list is sorted
    return True


def main():
    # sorted
    listOne = [1,2,3,4,5,6]
    print(f"List One is sorted: {is_sorted(listOne)}")

    # not sorted
    listTwo = [1,3,5,2,4,6]
    print(f"List Two is sorted: {is_sorted(listTwo)}")


if __name__ == "__main__":
    main()