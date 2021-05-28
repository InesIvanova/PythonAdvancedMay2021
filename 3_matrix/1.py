rows, cols = [int(el) for el in input().split(", ")]

matrix = []
result = 0

for row in range(rows):
    current_row_els = []
    matrix.append([int(el) for el in input().split(", ")])


for row in range(rows):
    for col in range(cols):
        result += matrix[row][col]

print(result)

print(matrix)