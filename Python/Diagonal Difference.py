#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    ltr=0
    rtl=0
    d=0
    l=len(arr)
    for i in range (0,l):
        ltr+=arr[i][i]
        rtl+=arr[i][l-1-i]
    if ltr>rtl:
        d=ltr-rtl
    else:
        d=rtl-ltr
        
    return (d)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
