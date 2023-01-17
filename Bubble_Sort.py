#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    
    for index in range(len(a)):
        for element in range(len(a)- index - 1):
            if a[element] > a[element + 1]:
                a[element], a[element + 1] = a[element + 1], a[element]
                count += 1
            
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a)- 1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
