def create_board():
    init_board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        init_board.append(row)
    return init_board


def print_board(init_board):
    for i in init_board:
        line_board = "|".join(i)
        print(line_board)
