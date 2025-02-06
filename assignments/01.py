"""
Assignment #01 - Hunter Wilson
Design and build a program to calculate a person’s Body Mass Index (BMI). 
The program must accept the individual's height in inches and their weight in pounds. 
It should then convert the measures to metric units, perform the calculation, 
and output the result.
"""

weight = float(input("Please enter weight (pounds): "))

height = float(input("Please enter heights (inches): "))

print("BMI is", (weight * 0.453592) / ((height * 0.0254) ** 2))