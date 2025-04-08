"""
PA #7 - Hunter Wilson

Write a GUI-based program that allows the user to convert temperature values between degrees Fahrenheit and degrees Celsius. 
The interface should have labeled entry fields for these two values. 
These components should be arranged in a grid where the labels occupy the first row and the corresponding fields occupy the second row. At start-up, 
the Fahrenheit field should contain 32.0, and the Celsius field should contain 0.0. 
The third row in the window contains two command buttons, labeled >>>> and <<<<. When the user presses the first button, 
the program should use the data in the Fahrenheit field to compute the Celsius value, 
which should then be output to the Celsius field. The second button should perform the inverse function.
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")

        self.addLabel(text="Test", row=1, column=0)

        # self.addLabel (Label for Celsius)
        # self.celsiusField (Celsius field)
        # self.addLabel (Label for Fahrenheit)
        # self.fahrField (Fahrenheit field)
        # self.addButton (Celsius button)
        # self.addButton (Fahrenheit button)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
      

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        
        
def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()