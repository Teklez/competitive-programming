# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

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
    i = n - 1
    container = arr[i]
    while i > -1:
        if container < arr[i - 1] and i -1 != -1:
            arr[i] = arr[i - 1]
            print(str(' '.join(map(str,arr))))
        else:
            arr[i] = container
            print(str(' '.join(map(str,arr))))
            break

        i -= 1
            

        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)



