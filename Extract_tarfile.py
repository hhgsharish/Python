import tarfile
import requests
import json

with open("1.json", "r") as fh:
    json_data= json.load(fh)

file_path = "behave.tar.gz"
for ele in json_data:
    source_url = ele["Source URL"]
    response = requests.get(source_url)

    with open(file_path, "wb") as file:
        file.write(response.content)
    print("Tar downloaded successfully")
    break

print("Outside of for loop")

file = tarfile.open("behave.tar.gz")

#extract file

file.extractall("/home/harish")
