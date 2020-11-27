from time import sleep

x = "X"

o = "0"


def clean_board():
    board = {"A": ['_'] * 3,
             "B": ['_'] * 3,
             "C": [' '] * 3}
    # print('cleaned!')
    return board


def print_board(board):
    print("  0 1 2")
    print_row("A", board)
    print_row("B", board)
    print_row("C", board)


def print_row(row_name, board):
    print(f"{row_name} {'|'.join(board[row_name])}")


# print_board(test_board)

# set_move("A1","X",test_board)
# updates board and returns True if valid move
# otherwise, no change to board and returns False
def set_move(move, value, board):
    row_id = move[0]
    col_i = int(move[1])
    occupied = is_occupied_space(row_id, col_i, board)
    if not occupied:
        board[row_id][col_i] = value
        return True
    if occupied:
        return False


def is_occupied_space(row_id, col_i, board):
    value = board[row_id][col_i]
    if value == o or value == x:
        return True
    else:
        return False


"""
Examples
is_valid_move(move,board)
is_valid_move("A1",test_board) -> True
is_valid_move("A3",test_board) -> False
is_valid_move("Q1",test_board) -> False
"""


def is_valid_move(move, board):
    if len(move) > 2:
        return False
    row_id = move[0]
    valid_move_1 = [str(num) for num in range(0, 3)]
    if move[1] not in valid_move_1:
        return False
    if row_id not in board:
        return False
    return True


sleep_time = 2

test_board = {"A": [' ', x, o],
              "B": [o, x, o],
              "C": [x, ' ', ' ']}

fresh_board = clean_board()


def play_sample_game():
    fresh_board = clean_board()
    # play a game, and print the board after each move...
    set_move("A1", x, fresh_board)
    print_board(fresh_board)
    sleep(sleep_time)

    set_move("A0", o, fresh_board)
    print_board(fresh_board)
    sleep(sleep_time)

    set_move("B2", x, fresh_board)
    print_board(fresh_board)
    sleep(sleep_time)

    set_move("C2", o, fresh_board)
    print_board(fresh_board)
    sleep(sleep_time)
