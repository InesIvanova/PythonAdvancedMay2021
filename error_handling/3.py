text = input()

number = input()
try:
    number = int(number)
except ValueError:
    print("Variable times must be an integer")
except SyntaxError:
    print("Some syntax error")
else:
    print(text * number)
finally:
    print("Printed no matter what")

