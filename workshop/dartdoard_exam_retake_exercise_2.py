import math


def is_in_range(row, col):
    if 0 <= row < 7 and 0 <= col < 7 :
        return True
    return False


def is_number(el):
    try:
        return int(el)
    except Exception:
        return False

N = 7

player_1, player_2 = input().split(", ")
points = {player_1: 501, player_2: 501}
players_turns = {0: player_2, 1: player_1}

turns_count = 0
matrix = []

for _ in range(N):
    matrix.append(input().split())

while True:
    row, col = [int(el) for el in input()[1:-1].split(", ")]
    turns_count += 1

    if is_in_range(row, col):
        number = is_number(matrix[row][col])
        if number:
            points[players_turns[turns_count % 2]] -= number

        current_points = sum([
            int(matrix[0][col]),
            int(matrix[-1][col]),
            int(matrix[row][0]),
            int(matrix[row][-1])
        ])

        if matrix[row][col] == "D":
            points[players_turns[turns_count % 2]] -= current_points*2

        if matrix[row][col] == "T":
            points[players_turns[turns_count % 2]] -= current_points*3

        if matrix[row][col] == "B":
            print(f"{players_turns[turns_count % 2]} won "
                  f"the game with {math.ceil(turns_count/2)} throws!")
            exit(0)

        if points[player_1] <= 0 or points[player_2] <= 0:
            break


print(f"{players_turns[turns_count % 2]} won "
                  f"the game with {math.ceil(turns_count/2)} throws!")
