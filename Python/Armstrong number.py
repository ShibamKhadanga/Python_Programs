#...........................................Checking the Armstrong No. using While Loop

n = int(input("Enter a Number: "))
c = 0
s = 0
i = n

while i > 0:
    c+=1          #Counting No. of digit 
    i = i//10
    
i = n
while i > 0:
    r = i%10
    s = s +(r**c)         # sum of each digit to the power of no. of digit
    i = i//10             # 153 = 1^3 + 5^3 + 3^3 = 153

if s == n:
    print("The given No. is a Armstrong number")
else:
    print("The given no. is not an Armstorng number")
    
    
    
