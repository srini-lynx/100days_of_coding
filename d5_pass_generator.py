#!/usr/bin/python

#Program: To generate Random Password

import random

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

symobols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+' ]

print("Welcome to the Password Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symobols = int(input("How many symobols would you like in your password?\n"))


for N in nr_letters:
  NEXT = random(letters)

print(f"The number of random letters selected :: {rand_letters}")
