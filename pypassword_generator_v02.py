#!/usr/bin/python
import random

#############
#Program to Generate a Random Password, Depending on the Number of Letters,Numbers and Symbols Given input
##############

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
          ]

numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

symbols = [ '~', '!' , '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+' ]

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Welcome to Random Password Genertor Utility....")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
nr_letters = int(input("How many letters are their in password? "))
nr_numbers = int(input("How many numbers are their in password? "))
nr_symbols = int(input("How many symbols are their in password? "))

print(f"Number of Letters Entered :: {nr_letters}")
print(f"Number of Numbers Entered :: {nr_numbers}")
print(f"Number of Symbols Entered :: {nr_symbols}") 

rand_letters =  random.sample(letters,nr_letters)
print(f"Randomly selected Letters :: {''.join(rand_letters)}")

rand_numbers = random.sample(numbers,nr_numbers)
print(f"Randomly selected Numbers :: {''.join(rand_numbers)}")

rand_symbols = random.sample(symbols,nr_symbols)
print(f"Randomly selected Symbols :: {''.join(rand_symbols)}")

rand_collection = []
rand_collection = rand_letters + rand_numbers + rand_symbols

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Putting all in one list rand_letters,rand_numbers and rand_symbols :: {rand_collection}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
nr_rand_collection = len(rand_collection)

print("=======================================================================================")
print(f"Number of Elements in rand_collection :: {nr_rand_collection}")
print("=======================================================================================")
total_rand = []
total_rand = random.sample(rand_collection,nr_rand_collection)

print("***************************************************************************************")
print("Final Random List.....")
print(f"{''.join(total_rand)}")
print("***************************************************************************************")
