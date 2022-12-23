import fileinput
import sys
import random
import numpy as np
import os
from Sound_Folder.sound import *
from Game_Folder.Rock_Paper_Scissors import *
  
# c
def replacement(file, previousw, nextw):
   for line in fileinput.input(file, inplace=1):
      line = line.replace(previousw, str(nextw))
      sys.stdout.write(line)


def random_color_card(color):
    """
  - args: type of file (white or black)
  - function is called from create_players_files()
  - returns a random card from the white or black file 
  - how it works:
    1. uses a loop to create an list with all the elements in the designated file 
    2. takes a random element from the list 
    3. return a random white or black card
  """
    with open("1" + color + '_cards.txt', 'r') as f:
        color_cards = []
        # what we iterating through and why
        for line in f:
            color_cards.append(np.array(line))
        card = color_cards[random.randint(0, len(color_cards))]
        return card


def create_players_files():
    """
  - args: none
  - function is called from main function 
  - returns a dictionary of the players names and their points {name: points} and the number of players inputed 
  - how it works:
    1. askes for the number of players 
    2. asks for their name
    3. creats a file (hand) for every player
    4. gives them 7 random white cards using random_color_card()
  """
    name_dict = {}
    num_players = int(input("Enter number of players: "))
    for i in range(num_players):
        phrase = " - Player " + str(i+1) + ", enter your name: "
        print("")
        name = input(phrase).upper()
        name_dict[name] = 0
        with open(name + '.txt', 'w+') as fil:
            for loop in range(7):  #gives each player 7 random white cards
                fil.write(str(random_color_card("white")))
    return name_dict, num_players


def get_card(name, num_of_the_card):  #get the card that the user choose
    """
  - args: name and index of the card chosen 
  - function is called from ask_card()
  - returns the information in the card from the players hand (the text in a specific line)
  - how it works:
    1. opens the file of the given player 
    2. creates an array with all the element in the user's file
    3. take the information from the line number (card) choosen and return it
  """
    userscard = []
    with open(name + '.txt', 'r') as f:
        for line in f:
            userscard.append(np.array(line))
        card = userscard[num_of_the_card]
    return card


def ask_card(name_dict):  #asks the user what card they want to use and returns the content of that specifc card
    """
  - args: dictionary with the name and the point of each user
  - function is called from main()
  - returns the the content of the card choosen
  - how it works:
    1. goes over every players name and asks them what card they want to use (from 1-7)
    2. player inputs the card they want to put down and that is added to a blank list
    3. the get_card() function converts the index of the card into it's information (writing)
  """
    chose_cards = []
    print("")
    print("CHOOSE CARDS:")
    for name in name_dict.keys():
        rep = " - " + name + " choose a card (from 1-7):"
        print("")
        try:
          rep = int(input(rep)) - 1
        except ValueError:
          print("\nSorry this is not a number. Please choose again.\n")
          rep = int(input(rep)) - 1
        chose_cards.append(rep)  #adds the num chosen by the user in a list
    content_in_card = []  #empty list to store the card's content
    number = 0
    for name in name_dict.keys():
        info_of_card = get_card(name, chose_cards[number])
        number += 1
        #remove el in file
        content_in_card.append(str(info_of_card))
    return content_in_card, chose_cards


def print_cards(content_in_card, name_dict, num_players):
    """
  - args: content_in_card (writing on card), name_dict (dictionary containing names and point values), and number of players 
  - function is called from voting()
  - prints the writing of the specific card each user selected 
  - returns a list of zeros equal to the amount of players 
  - how it works:
    1. prints the card every player chose
    2. creates a list of zeros, the length of the list is equal to the amount of players
  """
    point_list = []
#ramdom
    """print(content_in_card)
    random.shuffle(content_in_card)
    print(content_in_card)"""
    print("")
    for x in range(num_players):
        chosen = "Card " + str(x + 1) + ": " + str(content_in_card[x])
        print(chosen)
        point_list.append(0)
    return point_list


def voting(content_in_card, name_dict, num_players):
  """
  - args: content_in_card (writing on card) and name_dict (dictionary containing names and point values)
  - function is called from main()
  - returns a dictionary with the name of the players and amount of votes each player's response recieved in a list 
  - how it works:
    1. calls print_cards() function and gets a list of zeros equal to the amount of players 
    2. asks each player what their favorite card is 
    3. makes sure this card exists and if it doesn't then it promps the user to chose another card 
    4. point_list --> creates a list of zeros in order to set the length of the list
    5. use pop to remove the zeros and use insert to insert the amount of points into the list 
    6. finds the index of the person who recieved the most amount of points 
  """
  point_list = print_cards(content_in_card, name_dict, num_players)
  print("")
  print("FAVORITE CARDS:")
  for key in name_dict.keys():
      ans = " - " + key + " choose your favorite card: "
      print("")
      try:
        ans = int(input(ans)) - 1
      except ValueError:
        print("")
        print("Sorry this is not a number. Please choose again.")
        print("")
        ans = int(input(ans)) - 1
      while ans > num_players + 1:
          ans = key + "pick a card that exists: "
          ans = int(input(ans)) - 1
      numberofpoint = point_list.pop(ans)
      point_list.insert(ans, numberofpoint + 1)
  # print(point_list)

  #finds the indexes of the winners
  max_value = max(point_list)
  index_value = [index for index in range(len(point_list)) if point_list[index] == max_value ]
  
    # print(index_value)

    #creates a list of all the players names from the dictionary
  list_name = []
  for key in name_dict.keys():
      list_name.append(key)
  # print(list_name)

  #if there is a tie
  if len(index_value) == 2:
    list_name_winners = []
    for index in range(len(index_value)):
      name = list_name[index_value[index]]
      list_name_winners.append(name)
    print("\n")
    print("---- ROCK, PAPER, SCISSORS GAME STARTS ---- \n")
    print("There is a tie. Players will play rock, paper, scissors to determine the winner! \n1. Open the file 'tie_yourname.txt' \n2. In the file, rock, paper, and scissors will be shown \n3. Input the line number of the weapon you want to use \n4. See who wins! \n")  
    tie_sound()
    winner = Rock_Paper_Scissors(list_name_winners)
    value_of_key = name_dict.get(winner)
    name_dict[winner] = value_of_key + 1
      #value_of_key = name_dict.get(name)
      #name_dict[name] = value_of_key + 1
  ##else add one point to player who recieved the most votes
  else: 
    if len(index_value) == 1:
      for index in range(len(index_value)):
        name = list_name[index_value[index]]
        value_of_key = name_dict.get(name)
        name_dict[name] = value_of_key + 1
    
  return name_dict, list_name
  

#asks the players how many points they want to reach to end the game
def GetMaxPointOfPlayer(name_dict):
    points = []
    for values in name_dict.values():
        points.append(values)
    return max(points)

#deletes files when someone wins the game (end of a game)
def end_game(list_name):
  for name in list_name:
    file = name+".txt"
    os.remove(file)

def cards_against_humanity():
  print("CARDS AGAINST HUMANITY \n\nRULES: \n1. Only type responses into the console \n2. Only answer when its your turn \n3. Don't enter anyone else's file execpt your own 'yourname.txt'\n")
  print("CHOOSING CARDS: \nA black card will be presented. Each player will enter their own file titled 'yourname.txt' and input the card they want to play. \n** Note: players will input the line number of the card they want to play rather than the specific content on the line.\n")
  print("PICKING YOUR FAVORITE CARD: \nAfter every player chooses a card, all chosen cards will be displayed on the console. Each player (when prompted) will then input the number of their favorite card. Whoever gets the most votes, will be given a point.\n")
  name_dict, num_players = create_players_files()
  print("")
  max_point = int(input("Enter winning point value: "))
  point = 0
  round = 1
  while max_point > point:
    print("")
    print("------------------- ROUND", round, "-------------------")
    round += 1
    print("", "\n")
    print("BLACK CARD: ")
    print(random_color_card("black"))
    content_in_card, chose_cards = ask_card(name_dict)
    name_dict, list_name = voting(content_in_card, name_dict, num_players)

#calls the function replacement to 
    for num in range(len(list_name)):
      file = list_name[num] + ".txt"
      old = content_in_card[num]
      new = random_color_card("white")
      replacement(file, old, new)
    print("")
#print the point of each player   
    print("", "\n")
    for key, value in name_dict.items():
      if value == max_point:
        print(key, "YOU ARE THE WINNER!!")
        print("You have", value, "points", "\n")
        end_game_sound()
        break
      else:
        print(key, "has", value, "points", "\n")
      game_point_sound()
    point = GetMaxPointOfPlayer(name_dict)
  end_game(list_name)
    