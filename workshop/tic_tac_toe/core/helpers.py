from workshop.tic_tac_toe.core.constants import position_mapper


def get_row_col(pos):
    return position_mapper[pos]


def print_current_board_state(board):
    [print(f"| {' | '.join(el)} |") for el in board]