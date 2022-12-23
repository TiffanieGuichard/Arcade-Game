from Sound_Folder.sound import *

import numpy as np
import random
import os

ran = ["scissors", "paper", "rock"]


def end_game_for_game(list_name):
  #remove the file created for both players
  for name in list_name:
    file = "tie_" + name + ".txt"
    os.remove(file)

def get_card_for_game(name, num_of_the_card):
  #gets the information from the line the player choose
  userscard = []
  with open("tie_" + name + '.txt', 'r') as f:
      for line in f:
          userscard.append(np.array(line))
      card = userscard[num_of_the_card]
  return card

def random_file_for_game(ran, list_winners):
  #creats and append randomely the 3 posibilities in a file with the name of both players
  for index in list_winners:
    random.shuffle(ran)
    with open("tie_" + index + '.txt', 'w+') as fil:
      for index in ran:
        ans = index
        fil.write(ans+ "\n")

def Rock_Paper_Scissors(list_winners):
  if len(list_winners) != 2:
    name1 = input("\n - Player 1, enter your name: ")
    print("")
    name2 = input(" - Player 2, enter your name: ")
    print("\n")
    print("INSTRUCTIONS: \n1. Open the file 'tie_yourname.txt' \n2. In the file, rock, paper, and scissors will be shown \n3. Input the line number of the weapon you want to use \n4. See who wins! \n")  
    list_winners = [name1, name2]
  name1 = list_winners[0]
  name2 = list_winners[1]
  random_file_for_game(ran, list_winners)

  while True:
    print("")
    print("CHOOSE WEAPON: ")
    question1 = " - " + list_winners[0] + ", choose your weapon: "
    print("")
    user1= int(input(question1))-1
    weapon1 = get_card_for_game(name1, user1)
    question2 = " - " + list_winners[1] + ", choose your weapon: "
    print("")
    user2 = int(input(question2))-1
    weapon2 = get_card_for_game(name2, user2)
    weapon1 = str(weapon1)
    weapon2 = str(weapon2)
    weapon_2 = ""
    weapon_1 = ""
    for index in range(len(weapon2)-1):
      weapon_2 += weapon2[index]
    for index in range(len(weapon1)-1):
      weapon_1 += weapon1[index]
    print("")
    print("player1:", weapon_1, "\n")
    print("player2:", weapon_2, "\n")
 
    if weapon_1 == "scissors" and weapon_2 == "rock":
      print(name2,"Wins! \n")
      game_point_sound()
      print("---- ROCK, PAPER, SCISSORS GAME ENDS ---- ")
      end_game_for_game(list_winners)
      return name2
    elif weapon_1 == "scissors" and weapon_2 == "paper":
      print(name1,"Wins! \n")
      game_point_sound()
      print("---- ROCK, PAPER, SCISSORS GAME ENDS ---- ")
      end_game_for_game(list_winners)
      return name1
    elif weapon_1 == "rock" and weapon_2 == "paper":
      print(name2,"Wins! \n")
      game_point_sound()
      print("---- ROCK, PAPER, SCISSORS GAME ENDS ---- ")
      end_game_for_game(list_winners)
      return name2
    elif weapon_1 == "rock" and weapon_2 == "scissors":
      print(name1,"Wins! \n")
      game_point_sound()
      print("---- ROCK, PAPER, SCISSORS GAME ENDS ---- ")
      end_game_for_game(list_winners)
      return name1
    elif weapon_1 == "paper" and weapon_2 == "scissors":
      print(name2,"Wins! \n")
      game_point_sound()
      print("---- ROCK, PAPER, SCISSORS GAME ENDS ---- ")
      end_game_for_game(list_winners)
      return name2
    elif weapon_1 == "paper" and weapon_2 == "rock":
      print(name1,"WINS! \n")
      game_point_sound()
      print("---- ROCK, PAPER, SCISSORS GAME ENDS ---- ")
      end_game_for_game(list_winners)
      return name1
    else:
      print("YOU TIED! PLAY AGAIN!")
      tie_sound()
      random_file_for_game(ran, list_winners)
    
  end_game_for_game(list_winners)