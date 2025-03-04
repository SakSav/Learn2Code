# prompt: A Tic Tac Toe game written in Python and add a explaining comment for each section.

def print_board(board):
  # This function prints the current state of the board.
  print("-------------")
  for i in range(3):
    print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
    print("-------------")

def check_win(board, player):
  # This function checks if the given player has won the game.
  for i in range(3):
    if all(board[i][j] == player for j in range(3)):
      return True
    if all(board[j][i] == player for j in range(3)):
      return True
  if all(board[i][i] == player for i in range(3)):
    return True
  if all(board[i][2 - i] == player for i in range(3)):
    return True
  return False

def check_draw(board):
  # This function checks if the game is a draw.
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        return False
  return True

def play_tic_tac_toe():
  # This is the main function that runs the Tic Tac Toe game.
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"

  while True:
    print_board(board)
    print(f"Player {current_player}'s turn")
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
      board[row][col] = current_player

      if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
      elif check_draw(board):
        print_board(board)
        print("It's a draw!")
        break
      else:
        current_player = "O" if current_player == "X" else "X"
    else:
      print("Invalid move. Try again.")

if __name__ == "__main__":
  play_tic_tac_toe()
