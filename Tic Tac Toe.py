# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current
# state is solved, wouldn't we? Our goal is to create a function that will check that for us!
#
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty,
# 1 if it is an "X", or 2 if it is an "O"
#
# We want our function to return:
#
# -1 if the board is not yet finished (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).


def is_solved(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return "win hacia el lado"

        if board[0][row] == board[1][row] == board[2][row] != 0:
            return "win hacia abajp"

        if board[0][0] == board[1][1] == board[2][2] != 0:
            return "win diagonal"

        if board[0][2] == board[1][1] == board[2][0] != 0:
            return "win diagonal"

board = [[0, 0, 2],
         [2, 1, 2],
         [1, 2, 1]]

print(is_solved(board))