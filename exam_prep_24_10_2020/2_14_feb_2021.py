def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


n = int(input())

matrix = []
player_position = None

for row in range(n):
    row_data = input().split()
    if "P" in row_data:
        player_position = [row, row_data.index("P")]
    matrix.append(row_data)


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

coins = 0
steps = []

while True:
    direction = input()
    if direction in directions:
        next_row = player_position[0] + directions[direction][0]
        next_col = player_position[1] + directions[direction][1]
        if is_in_range(next_row, next_col, n) and not matrix[next_row][next_col] == "X":
            coins += int(matrix[next_row][next_col])
            steps.append([next_row, next_col])
        else:
            coins //= 2
            print(f"Game over! You've collected {coins} coins.")
            break
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break
        player_position = [next_row, next_col]

print(f"Your path: ")
[print(step) for step in steps]
