#!/usr/bin/python
import random

'''
#Program for Rock Paper and Scissor Game::

Rule:
1> Rock wins against Scissors
2> Scissors wins against Paper
3> Paper wins against Rock

'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("rock")
print(rock)
print("paper")
print(paper)
print("scissors")
print(scissors)

games_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer_choice = random.randint(0,2)


if user_choice >= 3 or user_choice < 0:
  print("You typed invalid number, you lose!!!")
elif user_choice == 0 and computer_choice == 2:
  print("You Win!!!")
  print("You choose")
  print(games_images[user_choice])
  print("Computer Choose")
  print(games_images[computer_choice])
elif computer_choice == 0 and user_choice == 2:
  print("You Loose!!!")
  print("You choose")
  print(games_images[user_choice])
  print("Computer Choose")
  print(games_images[computer_choice])
elif computer_choice > user_choice:
  print("You Loose!!!")
  print("You choose")
  print(games_images[user_choice])
  print("Computer Choose")
  print(games_images[computer_choice])
elif user_choice > computer_choice:
  print("You Win!!!")
  print("You choose")
  print(games_images[user_choice])
  print("Computer Choose")
  print(games_images[computer_choice])
elif computer_choice == user_choice:
  print("It's a Draw")  
  print("You choose")
  print(games_images[user_choice])
  print("Computer Choose")
  print(games_images[computer_choice])
