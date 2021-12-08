def create_board():
    # ----------------------------------------------------------------------
    # Creates empty list init_board and inserts another 3 lists called "row"
    # Each row has 3 blank spaces represented by "-"
    # ----------------------------------------------------------------------
    new_board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        new_board.append(row)
    return new_board


def print_board(init_board):
    # -------------------------------------------------------------------------
    # Replaces the commas in the list with lines for style, and shows the board
    # -------------------------------------------------------------------------
    for i in init_board:
        line_board = "|".join(i)
        print(line_board)
