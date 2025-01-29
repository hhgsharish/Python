# Initialize a list with mixed data types
my_list = [1, 2, "harish", "devops", 4, 5]

# Initialize a dictionary with keys and their corresponding values
my_dict = {
    "name": "john",
    "age": 26,
    "city": "Bangalore"
}

# Initialize an empty list
my_list1 = []

# Check if the element "harish" is present in my_list
if "harish" in my_list:
    print("Element Found")  # Print if the element is found
else:
    print("Element not Found")  # Print if the element is not found

# Check if my_list1 contains any values
if my_list1:
    print("List contains Values")  # Print if the list is not empty
else:
    print("Empty!!")  # Print if the list is empty

print("\n")  # Add a newline for better output formatting

# Check if the key "name" is present in my_dict
if "name" in my_dict:
    print("Key Found")  # Print if the key is found
else:
    print("Key Not Found")  # Print if the key is not found

print("\n")  # Add a newline for better output formatting

# Check if the value "name" is present in the values of my_dict
if "name" in my_dict.values():
    print("Value Found")  # Print if the value is found
else:
    print("Value Not Found")  # Print if the value is not found

print("\n")  # Add a newline for better output formatting

# Check if the value associated with the key "name" in my_dict is "harish"
if my_dict["name"] == "harish":
    print("Key contains the value")  # Print if the value matches
else:
    print("Key Not found")  # Print if the value does not match

# Initialize a boolean variable
found = True

# Check if 'found' is False
if not found:
    print("True")  # Print if 'found' is False
else:
    print("False")  # Print if 'found' is True

print("\n")  # Add a newline for better output formatting

# Check if my_dict is not empty
if my_dict:
    print("Dictionary is not empty")  # Print if the dictionary is not empty
else:
    print("Dict is empty")  # Print if the dictionary is empty
