#!/usr/bin/python 

#Program to find the highest score 

student_score = input("Enter the Score :: ").split()

for n in range(0, len(student_score)):
  student_score[n] = int(student_score[n])

#Highest Score 

highest_score = 0

for score in student_score:
  if score > highest_score:
    highest_score = score

print(f"Heighest score is :: {highest_score} ")
