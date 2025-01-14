'''#Date: 09/01/25
N = input("Enter Your Name: ")
B = input("Enter Your Branch: ")
S = input("Enter Your Semester: ")
E = input("Enter Your Enrollment No.: ")
print("\n\n\n\n User Data Is:-")
print("Name: ",N)
print("Branch: ",B)
print("Semester: ",S)
print("Enrollment no.: ",E)






N1 = int(input("Enter Your 1st Number: "))
N2 = int(input("Enter Your 2nd Number: "))
x = input("Choose from (+, -, *, /): ")
if(x=='+'):
    print("Sum is: ",N1+N2)
elif(x=='-'):
    print("Difference is: ",N1-N2)
elif(x=='*'):
    print("Product is: ",N1*N2)
elif(x=='/'):
    print("Quotient is: ",N1/N2)
else:
    print("Invalid Choice")







r = int(input("Enter Radius: "))
print("\nArea Of Circle is: ",3.14*r**2)
print("\nCircumference is: ",2*3.14*r)





N1 = int(input("Enter Your 1st Number: "))
N2 = int(input("Enter Your 2nd Number: "))

# Using 3 Variable
print("\n\n\n\nUsing 3 Variable")
print("\nBefore Swapping \nN1:",N1,"\nN2",N2)
x=N1
N1=N2
N2=x
print("\nAfter Swapping \nN1:",N1,"\nN2",N2)


# Using 2 Variable
print("\n\n\n\nUsing 2 Variable")
print("\nBefore Swapping \nN1:",N1,"\nN2",N2)
N1=N1+N2
N2=N1-N2
N1=N1-N2
print("\nAfter Swapping \nN1:",N1,"\nN2",N2)






print(" --- \t \t --- \t \t ----- ")
print("| X |\t+\t| Y |\t=\t| X+Y |")
print(" --- \t \t --- \t \t ----- ")'''





x=int(input("Enter 4 digit no.: "))
l=x%10
f=x//1000
print("Sum of 1st and last digit is: ",f+l)
































































'''def TenTimesEven(x):
    s=0
    p=len(x)
    for i in range (p):
        if x[i]%2==0:
            s=s+x[i]*10
    return("Sum of Ten times of Even Numbers:",s)
N=eval(input("Enter your Numbers"))
print(TenTimesEven(N))
x=1
for i in range (1,10):
    x+=1
    y=x//2
    print(y)
def change(p,q=10):
    p=p+q
    q=p-q
    print()
    return(p)
r=150
s=100
r=change(r,s)
print(r,"#",s)
s=change(s)

def prime():
    n=int(input("Enter your no.:"))
    for i in range (2,n):
        if n%i==0:
            print("no. is not prime")
        else:
            print("no. is prime")
prime()

v = 50
def dis(N):
    global v
    v=25
    if N%7==0:
        v=v+N
    else:
        v=v-N
print(v, end="#")
dis(20)
print(v)
dis(49)
print(v)




       

from datetime import date
x=date(2023,12,17)
print("Today's date is",x)'''
