# Tic-Tac-Toe with Unbeatable AI

## Overview

This is a Python implementation of a classic Tic-Tac-Toe game where the user plays against an AI. The AI uses the minimax algorithm to ensure it never loses.

## Features

- Unbeatable AI: The AI uses the minimax algorithm to always make the best possible move.
- Simple Interface: Simple text-based interface.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

  
   ``
   git clone https://github.com/dastgerdidev/unbeatable-tic-tac-toe
   ``
   
2. Navigate to the project directory:

   ``
   cd unbeatable-tic-tac-toe
   ``
   
## Usage

1. Run the game:

   ``
   python main.py
   ``
   
2. Follow the on-screen instructions to make your moves. The AI will automatically make its moves.

## How to Play

1. Start the Game: Run the game script using Python.
2. Make Your Move: When prompted, enter a number between 1 and 9 to place your 'O' on the board.
3. AI Move: The AI will automatically make its move.
4. Game Outcome: The game will continue until there is a winner or the board is full (resulting in a draw).

## Game Logic

- Board Representation: The board is represented as a list of 9 elements, where each element is either 'X', 'O', or ' ' (empty).
- Print Board: The print_board function prints the current state of the board.
- Check Winner: The check_winner function checks if a player has won by checking all possible winning conditions.
- Minimax Algorithm: The minimax function is a recursive function that evaluates the best move for the AI. It uses a depth-first search to explore all possible moves and their outcomes.
- Get Best Move: The get_best_move function uses the minimax algorithm to determine the best move for the AI.
- Make Move: The make_move function updates the board with the player's move.
- Main Game Loop: The play_game function handles the game loop, alternating between the player's move and the AI's move, and checking for a winner or a draw after each move.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The minimax algorithm is a well-known algorithm in game theory and artificial intelligence.
- Special thanks to the Python community for providing such a powerful and versatile language.

## Contact
- **GitHub:** [cj-c0de](https://github.com/cj-c0de)
- **Email:** dastgerdi.dev@gmail.com
