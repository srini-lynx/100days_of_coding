#!/usr/bin/python 

#Program: For Calculating the AVG height of Students 

TOTAL_HEIGHT = 0

STUDENT_HEIGHT = input("Enter Heights of Student separated by \",\" : ").split(",")

print(f"Entered Student Heights :: {STUDENT_HEIGHT}")

print(f"Type of STUDENT_HEIGHT Var :: {type(STUDENT_HEIGHT)}")


for STUDENT in STUDENT_HEIGHT:
  TOTAL_HEIGHT = int(STUDENT) + TOTAL_HEIGHT

AVG = TOTAL_HEIGHT / int(len(STUDENT_HEIGHT))

print(f"Average Height in the Class :: {AVG}")
