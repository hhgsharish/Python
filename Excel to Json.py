import pandas as pd  # Importing pandas for handling Excel files
import json  # Importing json module to save data in JSON format

def read_excel_content(excel_file, json_file_path):
    """
    Reads data from an Excel file, cleans the content, and saves it as a JSON file.

    Parameters:
    excel_file (str): Path to the input Excel file.
    json_file_path (str): Path to save the JSON output.
    """

    # Read the Excel file, specifically from 'Sheet1'
    data = pd.read_excel(excel_file, sheet_name="Sheet1")

    # Strip extra spaces from string values to clean the data
    data_cleaned = data.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Convert the cleaned DataFrame to JSON and save it in a structured format
    data_cleaned.to_json(json_file_path, orient="records", indent=4)

    print(f"Data successfully converted from {excel_file} to {json_file_path}")

# Specify the input Excel file and output JSON file paths
excel_file = "sample.xlsx"
json_file_path = "1.json"

# Call the function to process the Excel file
read_excel_content(excel_file, json_file_path)
