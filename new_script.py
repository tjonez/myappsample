#!/usr/bin/python

import os
import sys

def sum_list(list):
    sum = 0
    for item in list:
        sum += item
    return sum

list=[45, 2, 10, -5, 100]
print(sum_list(list))
print(list)
