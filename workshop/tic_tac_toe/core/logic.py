from workshop.tic_tac_toe.core.validators import is_position_in_range, is_place_available
from workshop.tic_tac_toe.core.helpers import get_row_col, print_current_board_state


def play(players, board, turns):
    current_turn_count = 1

    while True:
        current_player_name = turns[current_turn_count%2]
        position = int(input(f"{current_player_name} choose a free position: "))
        if is_position_in_range(position):
            if is_place_available(board, position):
                row, col = get_row_col(position)
                board[row][col] = players[current_player_name]
                print_current_board_state(board)
            # check if there is a winner
            # check if there is not a winner if the board is full
            a = 5
        else:
            # Read new position for the same player
            pass

        current_turn_count += 1


