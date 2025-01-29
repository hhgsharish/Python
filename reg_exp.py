import re  # Import the regular expressions library

# String containing email data
email_data = "john <john@gmail.com>, Rob <Rob@gmail.com, Jane <jane@gmail.com>"

# Search for the literal string "john" in the email_data
result = re.search(r"john", email_data)
print(result)  # Prints the match object if found, otherwise None

# Find all occurrences of the string "gmail" in email_data
result = re.findall(r"gmail", email_data)
print(result)  # Prints a list of all matches for "gmail"

# Search for "john" followed by either "n" or "m" in email_data
result = re.search(r"joh[n,m]", email_data)
print(result)  # Prints the match object for "john" (matches "n" in this case)

# Search for "joh" followed by any alphabetic character (lowercase or uppercase) in email_data
result = re.search(r"joh[a-zA-Z]", email_data)
print(result)  # Prints the match object for "john"

# Find all email addresses in email_data using a regular expression
result = re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)  # Prints a list of all valid email addresses

# Another way to find email addresses using a different regex pattern
result = re.findall(r"[\w+]+@[\w]+\.[\w]+", email_data)
print(result)  # Prints a list of all valid email addresses
