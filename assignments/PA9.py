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

        # Labels
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)

        # Entry Fields
        self.fahrField = self.addFloatField(value=32.0, row=1, column=0, width=10)
        self.celsiusField = self.addFloatField(value=0, row=1, column=1, width=10)

        # Buttons
        self.addButton(text="<<<<", row=2, column=1, command=self.computeFahr)
        self.addButton(text=">>>>", row=2, column=0, command=self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        celsius = self.celsiusField.getNumber()
        fahrenheit = (celsius * 9 / 5) + 32
        self.fahrField.setNumber(fahrenheit)
      

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        fahrenheit = self.fahrField.getNumber()
        celsius = (fahrenheit - 32) * 5 / 9
        self.celsiusField.setNumber(celsius)
        
def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()