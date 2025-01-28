n = int(input("Enter a Number: "))
c = 0
s = 0
i = n

while i > 0:
    c+=1
    i = i//10
    
i = n
while i > 0:
    r = i%10
    s = s +(r**c)
    i = i//10

if s == n:
    print("The given No. is a Armstrong number")
else:
    print("The given no. is not an Armstorng number")
    
    
    
