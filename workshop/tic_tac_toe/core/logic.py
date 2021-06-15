from workshop.tic_tac_toe.core.validators import is_position_in_range, is_place_available
from workshop.tic_tac_toe.core.helpers import (
    get_row_col,
    print_current_board_state,
    is_winner,
    is_board_full
)


def play(players, board, turns):
    current_turn_count = 1

    while True:
        current_player_name = turns[current_turn_count%2]
        position = int(input(f"{current_player_name} choose a free position: "))
        if current_turn_count >= 3:
            if is_position_in_range(position):
                if is_place_available(board, position):
                    row, col = get_row_col(position)
                    board[row][col] = players[current_player_name]
                    print_current_board_state(board)
                    if is_winner(board):
                        print(f"{current_player_name} wins")
                        exit(0)
                    if is_board_full(board):
                        print("Game over! No winner!")
                        exit(0)
            else:
                # Read new position for the same player
                pass

        current_turn_count += 1


