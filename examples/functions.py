""" 
Body Mass Index (BMI) calculator
"""

from convert import in2m, lbs2kg

def calc_bmi (height_m, weight_kg):
    """
    Calculate BMI
        weight - in kg
        height - in meters
    """
    return weight_kg / height_m**2

def main():
    height_in = float(input("Please enter height (inches): "))
    weight_lbs = float(input("Please enter weight (pounds): "))

    height_m = in2m(height_in)
    weight_kg = lbs2kg(weight_lbs)

    bmi = calc_bmi(height_m, weight_kg)

    print(f"The BMI is {bmi:.1f}")

main()