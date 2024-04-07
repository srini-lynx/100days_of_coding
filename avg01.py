#!/usr/bin/python

#Program: To find out AVG Height of class of students

STUD_HEIGHTS = input("Enter the Student Heights :").split()

print(f"The Students Heights Entered :: {STUD_HEIGHTS}")

NO_STUDENTS = 0
for n in STUD_HEIGHTS:
  NO_STUDENTS += 1

print(f"Number of Students :: {NO_STUDENTS}")

print(f"Type of STUD_HEIGHTS :: {type(STUD_HEIGHTS)}")

AVG_HEIGHT = 0
TOT_SUM = 0
for N in STUD_HEIGHTS:
  TOT_SUM += int(N) 

AVG_HEIGHT = TOT_SUM / NO_STUDENTS

print(f"Total heights added from list :: {TOT_SUM}")
print(f"Total number of Students :: {NO_STUDENTS}")
print(f"Average Height in the Student list :: {AVG_HEIGHT}")
