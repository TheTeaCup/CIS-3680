"""
File: polygons.py
Functions for drawing regular polygons.
"""

def square(t, length):
    """Draws a square with the given length."""
    for count in range(4):
        t.forward(length)
        t.left(90)

def hexagon(t, length):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons(t, n, length):
    """Draws a radial pattern of n squares with 
    the given length."""
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)

def radialPattern(t, n, length, shape):
    """Draws a radial pattern of n shapes with 
    the given length."""
    for count in range(n):
        shape(t, length)
        t.left(360 / n)
