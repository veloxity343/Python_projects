import random

def print_board(board):
    """
    Function to print the Tic Tac Toe board.
    """
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """
    Function to check if a player has won.
    """
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """
    Function to check if the board is full.
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_empty_cells(board):
    """
    Function to get a list of empty cells on the board.
    """
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def get_computer_move(board):
    """
    Function to get the computer's move.
    """
    # Check if there's a move to win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                if check_winner(board, 'O'):
                    board[i][j] = " "  # Reset the board
                    return i, j
                board[i][j] = " "  # Reset the board

    # Check if there's a move to block player from winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'X'
                if check_winner(board, 'X'):
                    board[i][j] = " "  # Reset the board
                    return i, j
                board[i][j] = " "  # Reset the board

    # Check if center is available
    if board[1][1] == " ":
        return 1, 1

    # Choose a random move from the available empty cells
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_tic_tac_toe():
    """
    Main function to play Tic Tac Toe.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        if current_player == "X":
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("That cell is already taken. Try again.")
                continue
            board[row][col] = current_player
        else:
            row, col = get_computer_move(board)
            board[row][col] = current_player
            print(f"Computer placed an '{current_player}' at position {row+1}, {col+1}")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()
