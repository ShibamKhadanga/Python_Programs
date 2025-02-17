#Question No.:- 01
'''Write a function contracting(l) that takes as input a list of integer l and returns
True if the absolute difference between each adjacent pair of elements strictly decreases.

Here are some examples of how your function should work.

  >>> contracting([9,2,7,3,1])
  True

  >>> contracting([-2,3,7,2,-1]) 
  False

  >>> contracting([10,7,4,1])
  False

Absolute difference means |2-3| = 1'''

def contracting(l):

   for i in range(1, len(l)):

       if abs(l[i] - l[i-1]) >= abs(l[i-1] - l[i-2]):

           return False

   return True











#Question No.:- 02
'''In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i]
is a hill if it is strictly greater than its neighbours and a valley if it is
strictly less than its neighbours.

Write a function counthv(l) that takes as input a list of integers l and
returns a list [hc,vc] where hc is the number of hills in l and vc is the number
of valleys in l.

Here are some examples to show how your function should work.

 
>>> counthv([1,2,1,2,3,2,1])
[2, 1]

>>> counthv([1,2,3,1])
[1, 0]

>>> counthv([3,1,2,3])
[0, 1]'''

def counthv(l):
    hc = 0
    vc = 0
    for i in range (1, len(l)-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            hc = hc + 1
        elif l[i] < l[i-1] and l[i] < l[i+1]:
            vc = vc + 1
    return [hc, vc]







#Question No.:- 03
'''A square n×n matrix of integers can be written in Python as a list with
n elements, where each element is in turn a list of n integers, representing
a row of the matrix. For instance, the matrix

  1  2  3
  4  5  6
  7  8  9
would be represented as [[1,2,3], [4,5,6], [7,8,9]].


Write a function leftrotate(m) that takes a list representation m of a square
matrix as input, and returns the matrix obtained by rotating the original
matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix
above, we get

  3  6  9
  2  5  8    
  1  4  7
Your function should not modify the argument m provided to the function rotate().


Here are some examples of how your function should work.

 
  >>> leftrotate([[1,2],[3,4]])
  [[2, 4], [1, 3]]

  >>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

  >>> leftrotate([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]'''

def leftrotate(m):
    x = [[0 for i in range (len(m))] for i in range (len(m))]
    for i in range (len(m)):
        for j in range (len(m)):
            x[i][j] = m[j][i]
    for i in range(len(x)):
             y=x[::-1]
    return y
print(leftrotate(m))
















