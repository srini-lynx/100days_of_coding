#!/usr/bin/python

number = int(input("Enter upto range to find out sum of odd and even numbers :"))
even_sum = 0
odd_sum = 0

for num in range(1,101):
  if num % 2 == 0:
    even_sum += num
  elif num %2 != 0:
    odd_sum += num

print(f"The Sum of all Even numbers within range from 1 to {number} :: {even_sum}")
print(f"The Sum of all Odd  numbers within range from 1 to {number} :: {odd_sum}")
