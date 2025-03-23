"""
File: enlarge.py
Project 7.11

Defines and tests a function to enlarge an image.
"""

from images import Image

def enlarge(image, factor):
    """Builds and returns a copy of the image which is larger
    by the factor."""
    pass

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    enlarge(image, 2)
    image.draw()

if __name__ == "__main__":
   main()


