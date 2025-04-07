"""
File: imagedemo.py
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Displays an image and a caption."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False)

        # Add the labels to the window.
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = "NSEW", columnspan=2)
        textLabel = self.addLabel(text = "Smokey the cat",
                                  row = 1, column = 0,
                                  sticky = "NSEW")
        textLabel2 = self.addLabel(text = "Double Trouble",
                                  row = 1, column = 1,
                                  sticky = "NSEW")
        
        # Load the image and associate it with the image label.
        self.image = PhotoImage(file = "smokey.gif")
        imageLabel["image"] = self.image

        # Set the font and color of the caption.
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel2["font"] = font
        textLabel["foreground"] = "blue"

def main():
    """Instantiates and pops up the window."""
    ImageDemo().mainloop()

if __name__ == "__main__":
    main()
