while True:
    try:
        x = int(input("Please enter a number, different then 0: "))
        print(5 / x)
        break
    except (ValueError, ZeroDivisionError):
        print("Invalid number")