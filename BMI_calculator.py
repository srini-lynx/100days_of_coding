#!/usr/bin/python

#Program to Calculate BMI of A Person

height = input("Enter Height of the person in Meters : ")
weight = input("Enter Weight of the person in KGS : ")
print("Height Entered : ",height," Meters")
print("Weight Entered : ", weight, " KGS" )

weight_int = int(weight) 
height_float = float(height)

BMI = weight_int / height_float ** 2

BMI_int = int(BMI)

print("BMI of the person : ", BMI_int)
