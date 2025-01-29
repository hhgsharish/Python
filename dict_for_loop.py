# Initialize a dictionary with keys and corresponding values
my_dict = {
    "name": "john",
    "age": 25,
    "city": "Bangalore"
}

# Loop through all the keys in the dictionary and print them
for key in my_dict.keys():
    print(key)  # Print each key

print("\n")  # Add a newline for better output formatting

# Loop through all the values in the dictionary and print them
for value in my_dict.values():
    print(value)  # Print each value

print("\n")  # Add a newline for better output formatting

# Loop through all key-value pairs in the dictionary and print them
for key, value in my_dict.items():
    print(key, value)  # Print each key along with its corresponding value
