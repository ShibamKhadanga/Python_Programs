#.......................................................Prime No. Between 1 to 100

print("Prime Nos. between 1 to 100 are: ")
n = 2
while n<=100:
    c=0
    j=1
    while j<=n:
        if(n%j==0):
            c+=1
        j+=1
    if(c==2):
        print(n,end=' ')
    n+=1
