# Purpose of the program:
# This program defines a class `example` that stores two string values, `str1` and `str2`, 
# and also a fixed string "DevOps". It provides methods to print the values in different formats.

class example:
    # Constructor (__init__) method to initialize the object with two string values (str1, str2)
    def __init__(self, str1, str2):
        self.name1 = str1  # Store the first string in the attribute 'name1'
        self.name2 = str2  # Store the second string in the attribute 'name2'
        self.name3 = "DevOps"  # Store the fixed string "DevOps" in the attribute 'name3'

    # Method to print the values of 'name1', 'name2', and 'name3'
    def print_value(self):
        print(self.name1, self.name2, self.name3)  # Prints all three stored values

    # Method to display only the value of 'name2'
    def display_value(self):
        print(self.name2)  # Prints only the value of 'name2'

# Create an object 'var' of the class 'example' and initialize it with values "Hello" and "World"
var = example("Hello", "World")

# Call the 'print_value' method to print all three attributes (name1, name2, and name3)
var.print_value()  # Expected output: Hello World DevOps

# Call the 'display_value' method to print only the value of 'name2'
var.display_value()  # Expected output: World
