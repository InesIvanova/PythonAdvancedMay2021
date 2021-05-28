n = int(input())

matrix = []
result = 0

for row in range(n):
    matrix.append([int(el) for el in input().split()])
    result += matrix[row][row]


# for row in range(n):
#     for col in range(n):
#         if row == col:
#             result += 3_matrix[row][col]


print(result)