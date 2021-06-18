
try:
    x = int("Peter")
except ValueError as err:
    print(err)
finally:
    print("Finally block")


