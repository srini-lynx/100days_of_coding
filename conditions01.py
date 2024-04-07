#!/usr/bin/python

#Program to Check Eligibility for Roller Coaster Ride and Calculate BILL as 
#Per AGE < 5 0, AGE >= 5 and <= 12 5, AGE > 12 7 

BILL = 0

print("Welcome to the RollerCoaster!")
HEIGHT = int(input("What's your height in Feet? "))

if HEIGHT >= 5:
  print("You are Eligible to take RollerCoaster Ride")
  AGE = int(input("What is your age? "))
  if AGE < 5:
    BILL = 0
    print(f"Child ticket is ${BILL}") 
  elif AGE >= 5 and AGE <= 12:
    BILL = 5
    print(f"Child ticket is ${BILL}")
  elif AGE > 12 and AGE <= 17:
    BILL = 7
    print(f"Child ticket is ${BILL}")
  else:
    BILL = 12
    print(f"Adult ticket is ${BILL}")

  Wann_Photo = input("Wann take a Photo Y/N: ")
  if Wann_Photo == "Y" or "y":
    print(f"BILL NOW IS : ${BILL}")
    BILL += 3 
  print(f"Your Final Bill: ${BILL}")


else:
  print("Sorry, you have to Grow atleast 5 Feet to take this Ride!!!!")
