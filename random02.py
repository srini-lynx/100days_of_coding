#!/usr/bin/python

import random

#Print the Value of floating point random number

random_float = random.random()

print(f"Value of random_float :: {random_float} ")

print("Default random float function prints value b/w 0 - 1 , As evedent from above output")
print("In order to print random value between 0 - N where N is as input")

range = int(input("Enter the number to find the random float from 0 to that number "))

random_number = random.random() * range

print(f"The random number in the range 0 to {range} is {random_number}")
