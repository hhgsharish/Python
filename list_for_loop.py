# Initialize a list of car models
models = ["creta", "nano", "Suzuki", "brezza"]

# Iterate through each model in the list and print it
for model in models:
    print(model)  # Print each car model from the list

print("\n")  # Add a newline for better output formatting

# Use enumerate to loop through the list with both index and value
for i, model in enumerate(models):
    print(i, model)  # Print the index and corresponding car model
