import numpy as np
import random 
from Game_Folder.wordss import *
from Sound_Folder.sound import *

from colored import fg

list_all_words = wordss


def print_hang_6(): 
  print("  +----+")
  print("  |    |")
  print("  |    O")
  print("  |   /|\\")
  print("  |   / \\")
  print("=====")

def print_hang_5(): 
  print("  +----+")
  print("  |    |")
  print("  |    O")
  print("  |   /|\\")
  print("  |   / ")
  print("=====")

def print_hang_4(): 
  print("  +----+")
  print("  |    |")
  print("  |    O")
  print("  |   /|\\")
  print("  |     ")
  print("=====")

def print_hang_3(): 
  print("  +----+")
  print("  |    |")
  print("  |    O")
  print("  |   /|")
  print("  |     ")
  print("=====")

def print_hang_2(): 
  print("  +----+")
  print("  |    |")
  print("  |    O")
  print("  |    |")
  print("  |     ")
  print("=====")

def print_hang_1(): 
  print("  +----+")
  print("  |    |")
  print("  |    O")
  print("  |     ")
  print("  |     ")
  print("=====")

def print_hang_0(): 
  print("  +----+")
  print("  |    |")
  print("  |     ")
  print("  |     ")
  print("  |     ")
  print("=====")




#gives random word from 'list_all_words'
def random_word(list_all_words): 
  secret_word = list_all_words[random.randint(0, len(list_all_words))]
  return secret_word

#converts ['_','_','_'] to '___' 
def show_list(game_list):  
    value = ""
    for x in range(len(game_list)):
      value = value + str(game_list[x]) + " "
    return value

def ask_letter():
  letter = input(" - Guess a letter: ")
  letter = letter.lower() 
  print("")
  return letter

#asks the player to guess a letter
def try_letter(tried_letters, secret_word, game_list, wrong_guesses):
  x = False
  letter = ask_letter()
  while letter in tried_letters:
    print("You have already guessed this letter.\n")
    letter = ask_letter()
  #letter_ = letter + " "
  tried_letters.append(letter)
  for index in range(len(secret_word)):
    if letter == secret_word[index]:
      x = True
      game_list[index] = letter
      game_point_sound()

  if not(x):
    print("Oh no! You guessed wrong.\n")
    wrong_guesses += 1
    if wrong_guesses == 1:
      print_hang_1()
    elif wrong_guesses == 2:
      print_hang_2()
    elif wrong_guesses == 3:
      print_hang_3()
    elif wrong_guesses == 4:
      print_hang_4()
    elif wrong_guesses == 5:
      print_hang_5()
    elif wrong_guesses == 6:
      print_hang_6()
  
  return game_list, tried_letters, wrong_guesses
  
def the_while(wrong_guesses, underscore,round, tried_letters, secret_word, game_list):
  #print(wrong_guesses, underscore)
  while wrong_guesses != 6 and underscore:
    round += 1
    print("\n------------ ROUND", round, "------------\n")
    game_list, tried_letters, wrong_guesses = try_letter(tried_letters, secret_word, game_list, wrong_guesses)
    print("")
    print("Word:",show_list(game_list), "\n")
    print("Letters guessed:",show_list(tried_letters), "\n")
    underscore = False
    for el in game_list:
      if el == "_ ":
        underscore = True
  if not(underscore):
    print("YOU WIN")
    print("")
    end_game_sound()
  if underscore:
    print("YOU LOST")
    extra_life = input("Do you still want to try ? (yes or no): ")
    while not(extra_life == "yes" or extra_life == "no"):
      print("Sorry, :", extra_life, "is not a possible answer. Please try again.4" )
      extra_life = input("Do you still want to try ? (yes or no): ")
    if extra_life == "yes":
      lifes = int(input("How many more chances ?"))
      wrong_guesses -= lifes
      wrong_guesses, underscore, round, tried_letters, secret_word, game_list = the_while(wrong_guesses, underscore, round, tried_letters, secret_word, game_list)
    else: 
      print("")
      rep = fg('red')  + "The word was " + secret_word
      print(rep)
      print("")
  return wrong_guesses, underscore, round, tried_letters, secret_word, game_list

  
#main function
def Hangman():
  print_hang_0()
  print("")
  secret_word = random_word(list_all_words)

  #print("secret_word:", secret_word)
  print("Word length:", len(secret_word))
  print("")
  
  #creates the '_____'
  game_list = []
  for el in range(len(secret_word)):
    game_list.append("_ ")
  
  print("Word:",show_list(game_list), "\n")
  
  wrong_guesses = 0
  tried_letters = []
  underscore = True
  round = 0
  wrong_guesses, underscore, round, tried_letters, secret_word, game_list = the_while(wrong_guesses, underscore,round, tried_letters, secret_word, game_list)
  

    
    
  
