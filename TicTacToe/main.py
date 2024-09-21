def print_board(board, size):
    for i,row in enumerate(board):
        print('|'.join(row))
        if i != size - 1:
            print('-' * (size * 2 - 1))

def get_board_size():
    while True:
        try:
            size = int(input("Please enter the board size N between 2 and 10: "))
            if 2 <= size <= 10:
                return size
            print("Error: Integer should be between 2 and 10")
        except ValueError:
            print("Error: Please enter a valid integer")

def get_user_input(which_player, size):
    while True:
        selection = input(f"Player {which_player} - Enter your move coordinates a,b from 1 to {size}: ")
        try:
            split_selection = selection.split(",")
            if len(split_selection) != 2:
                raise ValueError()
            tuple_selection = tuple(int(x) for x in split_selection)
            if tuple_selection[0] not in range(1, size + 1) or tuple_selection[1] not in range(1, size + 1):
                raise ValueError()
            return tuple_selection
        except ValueError:
            print(f"Error: Please enter only two coordinates from 1 to {size} seperated by a comma")

def check_empty(board, selection):
    if board[selection[0] - 1][selection[1] - 1] == ' ':
        return True
    return False

def make_move(board, player_selection, which_player):
        board[player_selection[0] - 1][player_selection[1] - 1] = which_player

def check_rows(board, size):
    for row in board:
        if row[0] != ' ' and row.count(row[0]) == size:
            return True
    return False

def check_columns(board, size):
    for col in range(size):
        first_element = board[0][col]
        if first_element != ' ':
            if all(board[row][col] == first_element for row in range(size)):
                return True
    return False

def check_diagonals(board, size):
    first_element = board[0][0]
    if first_element != ' ' and all(board[i][i] == first_element for i in range(size)):
        return True

    first_element = board[0][size - 1]
    if first_element != ' ' and all(board[i][size - i - 1] == first_element for i in range(size)):
        return True
    return False

def check_victory(board, size):
    if check_rows(board, size) == True or check_columns(board, size) == True or check_diagonals(board, size) == True:
        return True
    return False

def check_draw(board):
    return all(row.count(' ') == 0 for row in board)

def main():
    which_player = 'X'
    board_size = get_board_size()
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    while True:
        print_board(board, board_size)
        player_selection = get_user_input(which_player, board_size)
        if not check_empty(board, player_selection):
            print("Error: This tile is not empty!")
            continue
        make_move(board, player_selection, which_player)
        if check_victory(board, board_size):
            print_board(board, board_size)
            print(f"Player {which_player} wins!")
            return
        if check_draw(board):
            print_board(board, board_size)
            print("It is a draw!")
            return
        which_player = 'X' if which_player == 'O' else 'O'

if __name__ == "__main__":
    main()
