"""
OA #4 - Hunter Wilson

Create a program for the guessing game where the computer provides the guesses and can tell if you are cheating.

Example: 
Enter the smaller number: 1
Enter the larger number: 10
1 10
Your number is 5
Enter =, <, or >: >
6 10
Your number is 8
Enter =, <, or >: <
6 7
Your number is 6
Enter =, <, or >: >
7 7
Your number is 7
Enter =, <, or >: =
Hooray, I've got it in 4 tries!
"""
import random 

def main():
    # get input from the user about their small and large numbers
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))

    # keep count of the guesses
    count = 0

    while smaller <= larger:
        # generate a random number based off of the range of the small and larger number
        computer_number = random.randint(smaller, larger)

        # increment the the number of guesses
        count += 1

        # print out the guess of the users number
        print("Your number is", computer_number)

        # ask the user is the guess is correct
        operators = input("Enter =, <, or >: ")

        # if the user says the guess is equal then the bots guess is correct
        if operators == "=":
            print(f"Hooray, I've got it in {count} tries!")
            return
        
        # if the operator is less than then make the range smaller
        elif operators == "<":
            # if the computer number is smaller than or equal to the smaller number then the user is cheating
            if computer_number <= smaller:  
                print("Cheating detected! Exiting game.")
                return
            
            larger = computer_number - 1

        # if the operator is greater than then make the range larger
        elif operators == ">":
            # if the computer number is greater than or equal to the larger number them the user is cheating
            if computer_number >= larger:  
                print("Cheating detected! Exiting game.")
                return
            
            smaller = computer_number + 1

        else:
            print("Invalid input. Please enter '=', '<', or '>'.")

    print("Cheating detected! Your responses don't match a valid number.")

main()
