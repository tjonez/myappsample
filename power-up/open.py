#!/usr/bin/python

import os
import sys
import numpy
#this is the begining of my unstall script"
print(sys.version)

print('this is a test to see if i know what i am doing ')

def test():
    print("this is a test for me to know ")
test()

x = int(input("enter x: "))
y = int(input("enter y: "))

def add(a,b):
    ans = x+y
    print(ans)

def mult(a,b):
    ans1 = x*y
    print(ans1)

def div(a,b):
    ans2 = x/y
    print(ans2)

def sub(a,b):
    ans3 = x-y
    print(ans3)

print("here is the sum")
add(x,y)
print("here is the multiplication")
mult(x,y)
print("here is the division")
div(x,y)
print("here is the subtraction")
sub(x,y)
