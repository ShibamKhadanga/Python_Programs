'''Find 3 numbers whose sum and product are same'''
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            if i*j*k==i+j+k:
                if i!=0 and j!=0 and k!=0:
                    print (i, j, k)
                
