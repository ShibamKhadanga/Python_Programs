number= int(input("enter a number"))
reverse= 0
copy= number
while copy>reverse:
    remainder= copy % 10
    reverse = (reverse *10)+remainder
    copy = copy//10
    print("Reverse of",number,"is",reverse)
if number == reverse:
    print("number is palindrome")
