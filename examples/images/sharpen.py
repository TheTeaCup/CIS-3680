"""
File: sharpen.py
Project 7.10

Defines and tests a function to sharpen an image.
"""

from images import Image

def sharpen(image, degree, threshold):
    """Builds and returns a sharpened image.  Expects an image
    and two integers (the degree to which the image should be sharpened and the
    threshold used to detect edges) as arguments."""
    pass

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    sharpen(image, 20, 15)
    image.draw()

if __name__ == "__main__":
   main()


