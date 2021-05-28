rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for row in range(rows):
    current_row_el = []
    for el in input().split(" "):
        current_row_el.append(int(el))
    matrix.append(current_row_el)

for col in range(cols):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)