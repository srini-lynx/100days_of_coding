#!/usr/bin/python

#Program to tell Fizz, Buzz and FizzBuzz in the RANGE given
#If the number is divisible by 3: Fizz, by 5: Buzz if both 3 and 5 then FizzBuzz

num = int(input("Enter the range to find out Fizz,Buzz and FizBuzz :: "))

for N in range(1,num+1):
  if N % 3 == 0 and N % 5 == 0:
    print("FizzBuzz")
  elif N % 5 == 0:
    print("Buzz")
  elif N % 3 == 0:
    print("Fizz")
  else: 
    print(f"{N}")
