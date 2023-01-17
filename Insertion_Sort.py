#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for index in range(1, len(arr)):
        temp = arr[index]
        left = index - 1
        
        while left >= 0 and arr[left] > temp:
            arr[left + 1] = arr[left]
            left -= 1
            print(*arr)
            
        arr[left + 1] = temp
    print(*arr)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
