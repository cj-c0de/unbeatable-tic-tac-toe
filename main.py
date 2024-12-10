import math

# Define the game board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner('X'):
        return 1
    elif check_winner('O'):
        return -1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function to get the best move for the AI
def get_best_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Function to make a move
def make_move(index, player):
    if board[index] == ' ':
        board[index] = player
        return True
    return False

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")
    print_board()

    while True:
        # Player's move
        while True:
            try:
                player_move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= player_move < 9 and make_move(player_move, 'O'):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        print_board()

        if check_winner('O'):
            print("You win!")
            break
        elif is_board_full():
            print("It's a draw!")
            break

        # AI's move
        ai_move = get_best_move()
        make_move(ai_move, 'X')
        print(f"AI plays move {ai_move + 1}")
        print_board()

        if check_winner('X'):
            print("AI wins!")
            break
        elif is_board_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
