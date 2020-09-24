#board
#display board
#play game
#handle turn
#check win
  #check rows
  #check columns
  #check diagonals
#check tie
#flip player

#----- GLOBAL VARIABLES-----

#Game Board
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

#If game is still going
game_still_going = True

#Who won? or Tie?
winner = None

#Whos turn is it?
current_player = "X"

#Plays the game with the functions in the correct order
def play_game():

  display_board()

  while game_still_going:

    handle_turn(current_player)

    check_if_game_over()


    check_if_tie()

    #Changes to other player
    flip_player()

  #Game has ended
  if winner == "X" or winner == "O":
    print(winner + " won!")
  elif winner == None:
    print("Tie!")

  #Play again option check_if_play_again. Code project function at bottom.





#displays the board in a tic tac toe layout
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])



#handles the turn of current player
def handle_turn(player):
  print (player + "'s turn")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1


    if board[position] == "_":
      valid = True
    else: print ("You can't go there! Choose again.")



  board[position] = player

  display_board()



def check_if_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
#Set up global variables
  global winner

  #check rows
  row_winner = check_rows()
  #check comlumns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    #there was NO winner
    winner = None
  return




#---CHECK IF WIN FUNCTIONS----
def check_rows():
  #Sets up global variable
  global game_still_going

  #checks if any of the rows have same values
  row_1 = board[0] == board[1] == board[2] != "_"
  row_2 = board[3] == board[4] == board[5] != "_"
  row_3 = board[6] == board[7] == board[8] != "_"

  #if any of the rows have a match, will flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
    #Returns the winner (X or O)
  if row_1:
   return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  #Sets up global variable
  global game_still_going

  #checks if any of the rows have same values
  column_1 = board[0] == board[3] == board[6] != "_"
  column_2 = board[1] == board[4] == board[7] != "_"
  column_3 = board[2] == board[5] == board[8] != "_"

  #if any of the rows have a match, will flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
    #Returns the winner (X or O)
  if column_1:
   return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  #Sets up global variable
  global game_still_going

  #checks if any of the rows have same values
  diagonals_1 = board[0] == board[4] == board[8] != "_"
  diagonals_2 = board[6] == board[4] == board[2] != "_"


  #if any of the rows have a match, will flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
    #Returns the winner (X or O)
  if diagonals_1:
   return board[0]
  elif diagonals_2:
    return board[6]
  return
#---END OF CHECK IF WIN FUNCTIONS----


def check_if_tie():
  global game_still_going
  if "_" not in board:
    game_still_going = False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

def clear_board():
  cleaning = True
  while cleaning:
    board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    cleaning = False
  play_game()


def check_if_play_again():
  play_again = input("Play again? Y/N: ")
  play_again = play_again.upper()
  if play_again == "y" or "Y":
    clear_board()



play_game()


  
