#!/usr/bin/python
import random
print("Enter names each name should be separated by comma ',' :")
N = input()

names = N.split(',')

print(f"Names you entered :: {names}")

num_items = len(names)

print(f"There are {num_items} items in the names list")

WHO = random.randint(0,num_items - 1)
print(f"Value of WHO which is Random :: {WHO} ")

print(f"Hello {names[WHO]}, You need to pay the bill this time")
