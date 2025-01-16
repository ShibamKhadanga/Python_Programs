#....................................................To Find the GCD of two number

#..............................................1st way to solve the problem using Number
N1 = int(input("Enter Your 1st Number: "))
N2 = int(input("Enter Your 2nd Number: "))

if(N1<N2):
    x=N1
else:
    x=N2
    
for i in range(x,0,-1):
    f1 = N1%i
    f2 = N2%i
    if(f1==0 and f2==0):
        print("GCD of",N1,'&', N2 , "is", i)
        break



#..............................................2nd way to solve the problem using Library
import math
n1 = int(input("Enter Your 1st Number: "))
n2 = int(input("Enter Your 2nd Number: "))
r = math.gcd(n1,n2)
print("GCD of",n1,'&', n2 , "is", r)
