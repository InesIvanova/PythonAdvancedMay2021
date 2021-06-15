from workshop.tic_tac_toe.core.logic import play


def print_initial_boar_positions():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def create_empty_board():
    return [[" ", " ", " "] for _ in range(3)]


def setup():
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    player_1_sign = input(f"{player_1}, choose your sign (X or O): ").upper()
    while not player_1_sign in ["X", "O"]:
        player_1_sign = input(f"{player_1}, choose your sign (X or O): ").upper()
    player_2_sign = "O" if player_1_sign == "X" else "X"
    print(f"{player_1} starts first")
    print_initial_boar_positions()
    board = create_empty_board()
    players = {player_1: player_1_sign, player_2: player_2_sign}
    turns_mapper = {0: player_2, 1: player_1}
    play(players, board, turns_mapper)


def start_game():
    setup()


if __name__ == '__main__':
    start_game()

