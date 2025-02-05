'''Print the ratios of positive, negative and zero values in the array.
Each value should be printed on a separate line with  digits after the
decimal. The function should not return a value.'''


'''There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: 3/6 = 0.500000 ,
negative: 2/6 = 0.333333 and zeros: 1/6 = 0.166667 .'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    p=n=z=0
    for i in range (0,l):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            n+=1
        else:
            z+=1
    print(p/l)
    print(n/l)
    print(z/l)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
