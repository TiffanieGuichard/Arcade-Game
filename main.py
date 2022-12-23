from Sound_Folder.sound import *
from Game_Folder.cards_against_humanity import *
from Game_Folder.Tic_Tac_Toe import *
from Game_Folder.Rock_Paper_Scissors import *
from Game_Folder.Hangman import *
from colored import fg
'''
print("WELCOME TO THE ARCADE!!")
quit = ""    
while quit != "quit":
  #ask the user the number of the game they want to play
  print ("\nWhat game do you want to play? \n 1. Cards Against Humanity\n 2. Tic Tac Toe \n 3. Rock, Paper, Scissors\n 4. Hangman\n")
  num = 0
  while num != 1 or num != 2 or num != 3 or num != 4:
    try:
      num = int(input("Enter the number of the game: "))
    except ValueError:
      print("Invalid input. Please enter a number from 1 to 4.\n")
      #num = int(input("Enter the number of the game: "))
  #enters the game file associated with the number inputed
  if num == 1:
    cards_against_humanity()
  elif num == 2:
    Tic_Tac_Toe()
  elif num == 3: 
    list_winners = []
    Rock_Paper_Scissors(list_winners)
  elif num == 4:
    Hangman()
  quit = input(fg('white') + "If you want to quit enter 'quit', if not press enter.")
'''


print("WELCOME TO THE ARCADE!!")
quit = ""    
while quit != "quit":
  #ask the user the number of the game they want to play
  print ("\nWhat game do you want to play? \n 1. Cards Against Humanity\n 2. Tic Tac Toe \n 3. Rock, Paper, Scissors\n 4. Hangman\n")
  num = 0
  num = int(input("Enter the number of the game: "))
  if num == 1:
    cards_against_humanity()
  elif num == 2:
    Tic_Tac_Toe()
  elif num == 3: 
    list_winners = []
    Rock_Paper_Scissors(list_winners)
  elif num == 4:
    Hangman()
  quit = input(fg('white') + "If you want to quit enter 'quit', if not press enter.")