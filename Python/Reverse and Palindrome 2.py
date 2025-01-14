a=input("Enter a number")
n=list(a)
p=""
print("Reverse is")
for i in range(len(n)-1,-1,-1):
       p=p+n[i]
print(p)
print()
if a==p :
    print("The Number",a," is palindrome")
else:
    print("the number",a," is not palindrome") 
