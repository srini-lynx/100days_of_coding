#!/usr/bin/python

#Program to Print Basic Math Operations

A = int(input("Enter First  number: "))
B = int(input("Enter Second number: "))

C = A + B

print("Value of Variable A : ", A)
print("Value of Variable B : ", B)
print("Sum of A + B : ", C)

D = A - B

print("A - B Value is ", D)

E = A / B

print("A / B Value is ", E)

F = A ** B

print("A ** B Value is ", F)

PEMDAS1 = ( A * B + C / B - A)

print("PEMDAS1 Value is ", PEMDAS1)

PEMDAS2 = ( A * (B + C) / B - A)
print("PEMDAS2 Value is ", PEMDAS2)
