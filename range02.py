#!/usr/bin/python

#Program to Calculate even number total from a given range of numbers

number = int(input("Enter the number to find out total even numbers :"))
###print(f"The number entered :: {number} ")
even_total = 0

for num in range(2, number+1, 2):  #range(inital,upto,step value)
  even_total += num

print(f"The Sum of adding Even numbers in the range :: {even_total}")
