#!/usr/bin/python 

#Program to Calculate Sum of ODD numbers for a given RANGE

number = int(input("Enter the range to find the odd numbers sum :: "))
odd_sum = 0

for num in range(1,number+1, 2):
  #print(f"The number is :: {num} ")
  odd_sum += num

print(f"The Sum of all ODD numbers in the range 1 to {number} :: {odd_sum}")

