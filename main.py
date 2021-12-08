import board


def main():
    print("Welcome to Tic-Tac-Toe!")
    start_board = board.create_board()
    board.print_board(start_board)


main()
