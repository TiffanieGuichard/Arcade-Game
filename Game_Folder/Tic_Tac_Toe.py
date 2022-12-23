from Sound_Folder.sound import *


def Tic_Tac_Toe():
  board = [" " for _ in range(9)]  # create a table with 9 spaces " "
  
  def show_board(p, winner=None):
    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
    print("---+---+---")
    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
    print("---+---+---")
    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
    if winner:
      print("""* GAME OVER: player {0} won. *""".format(winner))
      end_game_sound()
  
  def morpion():
    player = "X"
    round = 0
    while True:
      show_board(board)
      print("\n> Player " + player + ", it's your turn. Enter a number from 1 to 9.")
      print("")
      move = int(input()) - 1  # notre tableau est de 0 à 8, donc on retire 1
      if board[move] == " ":
        board[move] = player
        round += 1
      else:
        print("** This spot has already been taken. **")
        continue  # on passe au prochain passage de boucle sans exécuter le code ci-dessous
      if board[0] == board[1] == board[2] != " " \
      or board[3] == board[4] == board[5] != " " \
      or board[6] == board[7] == board[8] != " " \
      or board[0] == board[3] == board[6] != " " \
      or board[1] == board[4] == board[7] != " " \
      or board[2] == board[5] == board[8] != " " \
      or board[0] == board[4] == board[8] != " " \
      or board[2] == board[4] == board[6] != " ":
        show_board(board, player)
        break
      if round == 9:
        print("TIE!")
        tie_sound()
        break
      player = "O" if player== "X" else "X"  # on change de player
  morpion()