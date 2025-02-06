"""
Conversion Library
"""

LBS_PER_KG = 2.2046
INCHES_PER_METER = 39.3701

def in2m (inches):
    return inches / INCHES_PER_METER

def lbs2kg (pounds):
    return pounds / LBS_PER_KG

def main():
    print("20 inches =", in2m(20), "meters")

if __name__ == "__main__":
    main()