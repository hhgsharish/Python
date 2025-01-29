import requests
import zipfile
import os

# File path to save the downloaded zip file
zip_file_path = "basic-text.zip"

# Iterate through the JSON data and download the first file

source_url = "https://sample-files.com/downloads/compressed/zip/basic-text.zip"
response = requests.get(source_url)  # Download the file
    
    # Save the downloaded content as a zip file
with open(zip_file_path, "wb") as file:
    file.write(response.content)
    print("Zip file downloaded successfully")
 
# Define the extraction directory
extraction_dir = "/home/harish"

# Create the extraction directory if it doesn't exist
os.makedirs(extraction_dir, exist_ok=True)

# Open the zip file and extract its contents
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(extraction_dir)  # Extract all files to the specified directory
    print(f"Files extracted to: {extraction_dir}")
