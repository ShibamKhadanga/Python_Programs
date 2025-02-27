#...Using numpy module doing multiplication'''

import numpy as np
m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]

print(np.dot(m1,m2))


#...Multiplication of 2X2 matrix
'''
m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]
r=[[0,0],[0,0]]
for i in range(2):       # Row Count
    for j in range(2):   # column Count
        for k in range(2):
            r[i][j]+=m1[i][k]*m2[k][j]
print(r)
'''

#...Multiplication of 3X3 Matrix
'''
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[2,5,7],[4,3,2],[0,5,5]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            r[i][j]+=m1[i][k]*m2[k][j]
print(r)'''
