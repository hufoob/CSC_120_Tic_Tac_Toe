import random

import board


def main():
    # -----------------------------------------------------------------
    # Introduces the player and handles the inputs for the users turns.
    # Calls functions to proceed through the game.
    # -----------------------------------------------------------------
    init_board = board.create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X\nPlayer 2 is O")
    print("Game Start!")
    if first_player() == 1:
        player_id = 1
    else:
        player_id = 2
    while True:
        print(f"Player {player_id}'s turn.")
        board.print_board(init_board)
        row = int(input("What row would you like to choose?: "))
        col = int(input("What column would you like to choose?: "))
        legal_move = check_mark(row - 1, col - 1, init_board)
        if legal_move:
            place_mark(row - 1, col - 1, player_id, init_board)
            winner = check_win(init_board)
            tie = check_tie(init_board)
            if winner:
                board.print_board(init_board)
                print(f"Player {player_id} wins!")
                break
            elif tie:
                board.print_board(init_board)
                print("It's a tie! No more moves.")
                break
            else:
                player_id = change_player(player_id)
                continue
        else:
            print("You can't do that, try again.")
            continue


def first_player():
    # -----------------------------------------------------------------
    # Sends a random integer to the main function to determine whether
    # Player 1 or 2 gets to go first.
    # -----------------------------------------------------------------
    return random.randint(1, 2)


def change_player(player_id):
    # -----------------------------------------------------------------
    # Function is called once the player has successfully completed their turn
    # Changes the id to give the other player their turn
    # -----------------------------------------------------------------
    if player_id == 1:
        return 2
    else:
        return 1


def check_mark(row, col, init_board):
    # -----------------------------------------------------------------
    # First checks for if the move is in a valid location. If the
    # location is valid, then it will check to see if it is "empty".
    # If the space is empty, it will return a True value and continue
    # the loop.
    # -----------------------------------------------------------------
    if row > 2 or col > 2:
        return False
    else:
        if init_board[row][col] == '-':
            return True
        else:
            return False


def place_mark(row, col, player_id, init_board):
    # -----------------------------------------------------------------
    # Changes the value in the list of lists to represent player input
    # -----------------------------------------------------------------
    if player_id == 1:
        init_board[row][col] = 'X'
    else:
        init_board[row][col] = 'O'


def check_win(init_board):
    # -----------------------------------------------------------------
    # I had trouble finding the most "pythonic" way to solve this, but
    # this function checks each way a user can win, by rows it does
    # this through iterating over the rows and checking if all elements
    # are the same. For vertical and diagonal, I ended up brute forcing
    # it to check if the exact 3 spots you can win diagonally and
    # vertically.
    # -----------------------------------------------------------------
    # Check row for winner by taking using set, which only takes unique elements
    # If all the elements in the row are the same, the length of the set will only be 1

    for row in init_board:
        if '-' not in row:
            if len(set(row)) == 1:
                return True
    # Checks for a winner via the columns by checking each column on the board using
    # a for loop, and ignores values that are "empty" i.e. equal to '-'
    for i in range(len(init_board)):
        if init_board[i][0] == init_board[i][1] == init_board[i][2] != "-" \
                or init_board[0][i] == init_board[1][i] == init_board[2][i] != "-":
            return True
    # Checks the exact points on the board that would need to be the same to ensure
    # a win diagonally, and ignores values that are "empty" i.e. equal to '-'
    if init_board[0][0] == init_board[1][1] == init_board[2][2] != '-' \
            or init_board[0][2] == init_board[1][1] == init_board[2][0] != '-':
        return True


def check_tie(init_board):
    # -----------------------------------------------------------------
    # Uses a nested for loop to check if there is a still an "empty"
    # spot on the board. If there are no free spots, returns True
    # which tells the main function to stop the game and call it a tie.
    # -----------------------------------------------------------------

    for row in init_board:
        for i in row:
            if i == '-':
                return False
    return True


main()
