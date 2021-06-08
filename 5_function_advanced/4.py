from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)


print(*["1", "2", "3"], sep="->")
print("->".join(["1", "2", "3"]))
