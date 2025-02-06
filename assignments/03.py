"""
Assignment #03 - Hunter Wilson

Construct a program that allows the user to enter the radius and height of a cylinder. 
The program should then calculate and output the total surface area of the cylinder
and its volume. Use the math module for the value of pi.
"""
import math

def calc_surface(radius, height):
    """
    Calculate the Surface Area
        - Radius
        - Height
    2 * PI * r(r + h)
    """
    return 2 * math.pi * radius * (radius + height)

def calc_volume(radius, height):
    """
    Calculate the Volume
        - Radius
        - Height
    PI * r^2 * height
    """
    return math.pi * (radius ** 2) * height

def main():
    # ask for the radius and the height
    radius = float(input("Please enter the radius of the cylinder: "))
    height = float(input("Please enter the height of the cylinder: "))

    # call the functions to calculate the surface area & volume
    surfaceArea = calc_surface(radius, height)
    volume = calc_volume(radius, height)

    # print out the Surface area & Volume of the cylinder
    print(f"Surface area of the cylinder is {surfaceArea:.2f} square units.")
    print(f"Volume of the cylinder is {volume:.2f} cubic units.")



main()