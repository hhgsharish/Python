
with open("File1.py","r") as fh:
    content = fh.read()
    print(f"{content}")


with open("1.txt", "w") as sh:
    sh.write("Hello World")

with open("1.txt", "r") as sh:
    con = sh.read()
    print(f"{con}")

with open("1.txt", "a") as sh:
    sh.write("\nThis is devops")

with open("1.txt", "r") as sh:
    con = sh.read()
    print(f"{con}")

