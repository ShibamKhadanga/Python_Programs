


''' ................................................. Linear Search ............................................... '''


l = list(map(int, input("Enter Sace Separated Numbers: ").split()))
# l=[12,10,35,2,21,32]
x=int(input("Enter no. want to search: "))
print('\nGiven List of no. is: \t',l)

f=0
for i in range(len(l)):
    if l[i]==x:
        f=1
        break
if f==1:
    print(f"\nNo. {x} found at pos: {i+1} and index: {i}")
else:
    print(f"\nNo. {x} is not present in the List {l}")
