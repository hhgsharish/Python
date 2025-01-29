#Write a script to list the text files in the path /home/ubuntu
import os

for root, dir, files in os.walk("/home/harish"):
    for file in files:
        if file.endswith('.txt'):
            print (f"{root}/{file}")
