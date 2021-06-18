from error_handling.errors import ValueCannotBeNegative

for _ in range(5):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative