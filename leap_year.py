#!/usr/bin/python

#Program in to find LEAP Year or not

YEAR = int(input("Enter Year to find out Leap Year or Not : "))

if YEAR % 4 == 0:
  if YEAR % 100 == 0:
    if YEAR % 400 == 0:
      print(f"Year entered  {YEAR} is LEAP ")
    else:
      print(f"Year entered {YEAR} is not LEAP ")
  else:
    print(f"Year entered {YEAR} is LEAP ")
else:
  print(f"Year entered {YEAR} is not LEAP")
