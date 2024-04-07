#!/usr/bin/python

#Program for TIP Calculator

print("Welcome to the TIP Calculator.")
BILL_AMOUNT = float(input("What was the total Bill amount? "))
PERCENT_TIP = int(input("What percentage tip would you like to give? 10,12, or 15 ? "))
SPLIT = int(input("How many people to split the bill ? "))

TIP = PERCENT_TIP / 100

TIP += 1

print(f"Tip to be used for Calculation:: {TIP} ")

TIP_BILL = round(BILL_AMOUNT * TIP,2)

print(f"The total Bill amount after adding Tip {TIP_BILL}")

TOTAL_BILL ="{:.2f}".format( TIP_BILL / SPLIT,2)

print(f"The Split between {SPLIT} people for the Bill After Adding Tip {PERCENT_TIP} % is {TOTAL_BILL} ")
