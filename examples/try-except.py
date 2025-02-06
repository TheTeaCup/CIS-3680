#

age = input("Please enter your age: ")
try:
    age = int(age)
    print("You are", age, "years old.")
except ValueError:
    print("Please enter a valid age.")


