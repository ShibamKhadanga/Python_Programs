


''' ................................................. Binary Search ............................................... '''


#l = list(map(int, input("Enter Sace Separated Numbers: ").split()))
l=[12,10,35,2,21,32]
x=int(input("Enter no. want to search: "))
print('\nGiven List of no. is: \t',l)

l.sort()
print('\nSorted List of no. is: \t',l)

left=0
right=len(l)-1

f=0

while left<=right:
    mid = (left + right)//2
    if l[mid]==x:
        f=1
        break
    elif l[mid]>x:
        right = mid-1
    else:
        left = mid+1

if f == 0:
    print('\nNot Found')
else:
    print('\nFound at: ',mid)
