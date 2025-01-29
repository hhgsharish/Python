# Open the file "File1.py" in read mode and read its content
with open("File1.py", "r") as fh:
    content = fh.read()  # Read the entire content of the file
    print(f"{content}")  # Print the content of the file

# Open the file "1.txt" in write mode and write "Hello World" to it
with open("1.txt", "w") as sh:
    sh.write("Hello World")  # Write "Hello World" to the file

# Open the file "1.txt" in read mode and print its content
with open("1.txt", "r") as sh:
    con = sh.read()  # Read the content of the file
    print(f"{con}")  # Print the content

# Open the file "1.txt" in append mode and add a new line with "This is devops"
with open("1.txt", "a") as sh:
    sh.write("\nThis is devops")  # Append a new line to the file

# Open the file "1.txt" again in read mode and print its updated content
with open("1.txt", "r") as sh:
    con = sh.read()  # Read the updated content of the file
    print(f"{con}")  # Print the updated content
