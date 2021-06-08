def multiply(*args):
    result = 1
    for el in args:
        result *= el
    return result


# Second option
# from functools import reduce
#
# def multiply(*args):
#     return reduce(lambda x, y: x*y, args)

# print(list(map(lambda x, y: x*y, (1, 4, 5))))



# Why we should now how many params are expected in map/reduce

# def map(func, iterable):
#     result = []
#     for el in iterable:
#         result.append(func(el))
#     return result
#
# def reduce(func, iterable):
#     result = []
#     for index in range(len(iterable), 2):
#         result.append(func(iterable[index], iterable[index + 1]))


#This is wrong for map
# print(map(lambda x, y: int(x+y), ("1", "2", "3")))
# print(reduce(lambda x, y: x + y, [1, 2, 3]))

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
