from os import path

# First
if path.exists("file.txt"):
    print("File found")
else:
    print("File not found")


# Second way

try:
    open("file.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")
