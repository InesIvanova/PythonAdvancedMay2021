from workshop.tic_tac_toe.core.constants import position_mapper


def get_row_col(pos):
    return position_mapper[pos]


def print_current_board_state(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def is_board_full(board):
    is_full = True
    for row in board:
        if " " in row:
            is_full = False
    return is_full


def is_row_winner(board):
    for row in board:
        if row.count('X') == len(row) or row.count('O') == len(row):
            return True
    return False


def is_col_winner(board):
    is_found = False

    first = [board[0][0], board[1][0], board[2][0]]
    second = [board[0][1], board[1][1], board[2][1]]
    third = [board[0][2], board[1][2], board[2][2]]

    if first.count('X') == len(board) or first.count('O') == len(board):
        is_found = True
    elif second.count('X') == len(board) or second.count('O') == len(board):
        is_found = True
    elif third.count('X') == len(board) or third.count('O') == len(board):
        is_found = True
    return is_found


def is_primary_diagonal_winner(board):
    current_values = []
    for row in range(len(board)):
        current_values.append(board[row][row])
    if current_values.count("X") == len(board) or current_values.count("O") == len(board):
        return True
    return False


def is_second_diagonal_winner(board):
    current_values = []
    n = len(board)
    for i in range(len(board)):
        current_values.append(board[n-i-1][i])

    if current_values.count("X") == len(board) or current_values.count("O") == len(board):
        return True
    return False


def is_winner(board):
    if is_row_winner(board) or is_col_winner(board) \
            or is_primary_diagonal_winner(board) or is_second_diagonal_winner(board):
        return True
    return False
