from board import clean_board, print_board, x, o, set_move, is_valid_move, is_occupied_space
from display import win_screen, lose_screen


def welcome():
    msg = """
    Welcome to AI Tic Tac Toe
    """
    print(msg)


# example of another change
def get_user_name():
    print("Tell me your name")
    name = input("name: ")
    print(f"Hello {name}!")
    return name


# first move
def prompt_first_move(name, game_board):
    print(f"{name} tell me your first move?")
    print_board(game_board)
    move = input("move or 'quit': ")
    if move == 'quit':
        good_bye(name)
    if is_valid_move(move, game_board):
        set_move(move, o, game_board)
    else:
        print("invalid move")
        prompt_first_move(name, game_board)


def switch_symbol(symbol):
    if symbol == o:
        symbol = x
    else:
        symbol = o
    return symbol


# We assume all moves are legal and in the correct order
# No moves remaining when there are no spaces left
# that are not x or o
def any_moves_remaining(game_board):
    # go through the remaining spaces
    # and if any aren't x or o
    # return True
    # otherwise return False
    for row_id in game_board:
        for col_i in [0, 1, 2]:
            if not is_occupied_space(row_id, col_i, game_board):
                return True
    return False


def win_check(game_board, symbol):
    # horizontal win
    for row_id in game_board:
        row = game_board[row_id]
        if all([s == symbol for s in row]):
            return True
    # vertical win
    for col_i in [0, 1, 2]:
        if all([game_board[row_id][col_i] == symbol for row_id in game_board]):
            return True
    # diagonal win
    # if \ win
    if (game_board["A"][0] == symbol) and (game_board["B"][1] == symbol) and (game_board["C"][2] == symbol):
        return True
    # if / win
    if (game_board["A"][2] == symbol) and (game_board["B"][1] == symbol) and (game_board["C"][0] == symbol):
        return True
    # finally
    return False


def win_loop(name):
    gameboard = clean_board()
    prompt_first_move(name, gameboard)
    game_loop(gameboard, name)


# rest of the moves
def game_loop(game_board, name):
    move = ''
    symbol = x
    while move != 'quit':
        print_board(game_board)
        print(f"{symbol} make a move")
        move = input("move or 'quit': ")
        if move == 'quit':
            return None
        if is_valid_move(move, game_board):
            move_success = set_move(move, symbol, game_board)
            if move_success:
                if not any_moves_remaining(game_board):
                    print("TIE!!")
                    win_loop(name)
                if win_check(game_board, symbol):
                    if o is symbol:
                        win_screen(name)
                    else:
                        lose_screen(name)
                    win_loop(name)
                else:
                    symbol = switch_symbol(symbol)
            else:
                print(f"{move} is already occupied")
        else:
            print("not a valid move type other move")


def good_bye(name):
    print(f"Goodbye {name}")
    exit()


if __name__ == '__main__':
    board = clean_board()
    welcome()
    user_name = get_user_name()
    prompt_first_move(user_name, board)
    game_loop(board, user_name)
    good_bye(user_name)
