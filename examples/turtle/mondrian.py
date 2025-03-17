"""
File: mondrian.py
Project 7.4
Author:

This program displays a Mondrian-like painting with 
the user's input level.
"""

import turtle
import random

def fillRectangle(t, x1, y1, x2, y2):
    """Fills a rectangle with the given corner points
    using a random color."""
    turtle.setup(width=300, height= 300, startx=0, starty=0)
    ts = turtle.Screen() 
    ts.colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

def mondrian(t, x1, y1, x2, y2, level):
    """Draws a Mondrian-like painting at the given level."""



def main():
    level = int(input("Enter a level: "))
    t = turtle
    width = 200
    height = 200 
    mondrian(t, -width, height, width, -height, level)
    turtle.done()

if __name__ == "__main__":
   main()


