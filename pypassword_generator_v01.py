#!/usr/bin/python
import random

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

numbers = [ '0','1','2','3','4','5','6','7','8','9' ]

symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '@', '^', '_','+' ]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many Letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your pasword? "))
nr_symbols = int(input("How many sympbols would you like in your symbols? "))

print(f"The Number of letters : {nr_letters}, The number of numbers : {nr_numbers}, The number of Symbols : {nr_symbols}")

I = nr_letters
result = []
while I >= 1:
  #print(random.choice(letters))
  result.append(random.choice(letters))
  I = I - 1  

K = nr_numbers
result1 = []
while K >= 1:
  #print(random.choice(numbers))
  result1.append(random.choice(numbers))
  K = K - 1

P = nr_symbols
result2 = []
while P >= 1:
  #print(random.choice(symbols))
  result2.append(random.choice(symbols))
  P = P - 1

#for I in range(len(letters)):
#  print(I)

print("*************************************************************************")
print(f"LETTER")
print(result)
print("*************************************************************************")
print("*************************************************************************")
print(f"NUMBER")
print(result1)
print("*************************************************************************")
print(f"SYMBOLS")
print(result2)
print("*************************************************************************")
print("*************************************************************************")

TOTAL = result + result1 + result2

print(f"Total :: {TOTAL}")
print("*************************************************************************")
print("*************************************************************************")

print(''.join(TOTAL))

nr_total = int((len(TOTAL)) )
#print(len(TOTAL))
print(f"Total_LENGHT is :: {nr_total}")

final_result = []

final_result = random.sample(TOTAL,nr_total)

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(''.join(final_result))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

'''
final_result = []
Q = nr_total - 1
while Q >= 0:
  final_result.append(random.choice(TOTAL))
  Q = Q - 1

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Final Password Generated...")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(''.join(final_result))
'''
