def valid_moves(board, player):
    """This function determines the valid moves a player can make on a given tic-tac-toe board.
       A valid move is defined as one where the chosen cell of the board is not already occupied.

       Params:
       board - A 2D list of strings representing the game state.
       player - A string representing the current player ("X" or "O").
       
       Returns:
       A list of tuples, where each tuple represents the coordinates (i, j) of a valid move."
    """
    valid_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                valid_moves.append((i,j))
    return valid_moves
def count_winning_moves(board, player):
    """Create a function count_winning_moves that takes as input the current state of a tic-tac-toe
       board and the current player ("X" or "O") and returns the number of winning moves available 
       to the current player. In order to count as a winning move, placing the player's symbol ("X" or "O")
       on a designated cell would result in that player winning the game.
       
       A winning condition in tic-tac-toe is defined as any row, column, or diagonal filled 
       exclusively with the player's symbol.
       
       If the board is already winning for the player, return -1
       
       The tic-tac-toe board is a 2D list of strings where each string is either "X", "O", or " ".

       For example:
       count_winning_moves([
                               ["X", " ", " "],
                               [" ", "X", " "],
                               [" ", " ", "X"]
                           ], "X") 
       returns -1
       count_winning_moves([
                               ["O", " ", " "],
                               [" ", "X", " "],
                               [" ", " ", "X"]
                           ], "X") 
       returns 0
       count_winning_moves([
                               ["X", "O", "X"],
                               ["O", "X", "O"],
                               [" ", " ", " "]
                           ], "X") 
       returns 2
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return -1
        if board[0][i] == board[1][i] == board[2][i] == player:
            return -1
    if board[0][0] == board[1][1] == board[2][2] == player:
        return -1
    if board[0][2] == board[1][1] == board[2][0] == player:
        return -1
    winning_moves = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                board[i][j] = player
                if board[i][0] == board[i][1] == board[i][2] == player:
                    winning_moves += 1
                if board[0][j] == board[1][j] == board[2][j] == player:
                    winning_moves += 1
                if i == j and board[0][0] == board[1][1] == board[2][2] == player:
                    winning_moves += 1
                if i == len(board) - j - 1 and board[0][2] == board[1][1] == board[2][0] == player:
                    winning_moves += 1
                board[i][j] = ' '
    return winning_moves