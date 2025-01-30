# BMI Calculator
# Hunter Wilson

weight = float(input("Please enter weight (pounds): "))

height = float(input("Please enter heights (inches): "))

print("BMI is", (weight * 0.453592) / ((height * 0.0254) ** 2))