import os

try:
    os.remove("asd.txt")
except FileNotFoundError:
    print("File already deleted!")


# Option 2

# if os.path.exists("asd.txt"):
#     os.remove("asd.txt")
# else:
#     print("File already deleted!")