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
        if legal_move == 1:
            place_mark(row - 1, col - 1, player_id, init_board)
            player_id = change_player(player_id)
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


# def check_win (row,col,player_id):


main()
