#!/usr/bin/python

#Program: Pizz calculator : S,M,L

print("***************************")
print("Welcome to PIZZ Ordering!!!")
print("***************************")
print("Price:: S => $10   ($2 Pepercon + $1 Cheese)")
print("Price:: M => $15   ($3 Pepercon + $1 Cheese)")
print("Price:: L => $20   ($4 Pepercon + $1 Cheese)")
print("*********************************************")

PIZ = input("What's the PIZZ Size : S, M or L ? ")
PEP = input("Do you need pepercon  additional  Y/N ? ")
CHES = input("Do you need Additional Cheese  Y/N ? ")
BILL = 0
NOBILL = 0

if PIZ == "S":
  BILL += 10
elif PIZ == "M":
  BILL += 15
elif PIZ == "L":
  BILL += 20
else:
  NOBILL = 1
  print("UNKNOW selection")

if PEP == "Y":
  if PIZ == "S":
    BILL += 2
  elif PIZ == "M":
    BILL += 3
  elif PIZ == "L":
    BILL += 4
  else:
    NOBILL = 1
    print("UNKOWN Selection")

if CHES == "Y":
  BILL += 1

if not NOBILL:
  print(f"Your's final bill for piz type {PIZ} is : ${BILL}")
