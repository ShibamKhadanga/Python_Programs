


''' ................................................. Selection Sort............................................... '''

# l = list(map(int, input("Enter Sace Separated Numbers: ").split()))
l=[12,10,35,2,21,32]


print('Given List of no. is: \t',l)


for i in range(len(l)-1):
    print('\n\nStep:',i+1,'--->',l)

    mini = l[i]
    for j in range(i+1,len(l)):
        
        if l[j]<mini:
            mini=l[j]
    print(f"\n\t\tMinimum: {mini}")
    print(f'\t\tSwapping {mini} with {l[i]}(FOR INDEX-{i})')

    x=l.index(mini)
    if l[x] < l[i]:
        l[x],l[i]=l[i],l[x]
    print( '\n\t    ',l)

print('\n\nSorter List of no. is: \t',l)

