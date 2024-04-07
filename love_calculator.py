#!/usr/bin/python

#Program for Calculating Love Compatibility

print("******* Welcome to Love Compatibility Calculator ***********")

NAME1 = input("Enter First Name:: ")
NAME2 = input("Enter Second Name:: ")

COMB_NAMES = NAME1 + NAME2

LOWER_NAMES = COMB_NAMES.lower()
t = LOWER_NAMES.count("t")
r = LOWER_NAMES.count("r")
u = LOWER_NAMES.count("u")
e = LOWER_NAMES.count("e")

First_Digit = t + r + u + e

l = LOWER_NAMES.count("l")
o = LOWER_NAMES.count("o")
v = LOWER_NAMES.count("v")
e = LOWER_NAMES.count("e")

Second_Digit = l + o + v + e

Score = int(str(First_Digit) + str(Second_Digit))

if (Score < 10) or (Score > 90):
  print(f"Your Score is {Score}, you go together like coke and mentos.")
elif (Score >= 40) and (Score <= 50):
  print(f"Your Score is {Score}, you are alright together..")
else:
  print(f"Your Score is {Score}.")
