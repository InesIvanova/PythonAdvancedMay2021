# from itertools import combinations
#
# result = list(combinations(input().split(", "), int(input())))
# for x,y in result:
#     print(x, y, sep=", ")


def combinations(names, count, current_names=[]):
    if len(current_names) == count:
        print(", ".join(current_names))
        return

    for i in range(len(names)):
        current_names.append(names[i])
        combinations(names[i+1:], count, current_names)
        current_names.pop()


names = input().split(", ")
n = int(input())
combinations(names, n)

