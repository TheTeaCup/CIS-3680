"""
PA #7 - Hunter Wilson

Draws a circle.

1. The inputs are the coordinates of the center point and the radius.

Define a function draw_circle. 
This function should expect a Turtle object, 
the coordinates of the circle's center point, 
and the circle's radius as arguments.  
The function should draw the specified circle. 
The algorithm should draw the circle's circumference by turning 3 degrees and
moving a given distance 120 times.  
Calculate the distance moved with the formula 2.0 * pi * radius / 120.0.
"""

import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    """Draws a circle with the given center point and radius."""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()

    distance = 2.0 * math.pi * radius / 120.0

    # draw circle
    count = 0
    while(count != 120):
        count += 1
        t.forward(distance)
        t.left(3)

def main():
    x = 50
    y = 75
    radius = 100
    drawCircle(Turtle(), x, y, radius)
    input("Press the enter key to close the program.")

if __name__ == "__main__":
    main()
