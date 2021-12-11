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
    numSwaps = 0
    n = len(a)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps +=1
           
    firstElement = a[0]
    lastElement = a[-1]
    # print(a)
    print("Array is sorted in "+ str(numSwaps) + " swaps.")
    # print(f"Array is sorted in {numSwaps} swaps.")
    print("First Element: " + str(firstElement))
    print("Last Element: " + str(lastElement))
    #return numSwaps, firstElement, lastElement
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
