# 

wall_length = float(input("Please enter the length of the wall (feet): "))
wall_height = float(input("Please enter the height of the wall (feet): "))

wall_area = wall_length * wall_height

door_count = int(input("Please enter the number of doors: "))
door_allowance = door_count * 14

window_count = int(input("Please enter the number of windows: "))
window_allowance = window_count * 8.5

total_area = wall_area - door_allowance - window_allowance

gallons = total_area / 350

paint_price = float(input("Please enter the price of the paint per gallon: "))

cost = gallons * paint_price

print("You will need", gallons, "gallons of paint for the job.")
print("The cost of the paint will be $", cost)