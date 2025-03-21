


''' ................................................. Selection Sort............................................... '''

l = list(map(int, input("Enter Sace Separated Numbers: ").split()))
# l=[12,10,35,2,21,32]


print('Given List of no. is: \t',l)


for i in range(len(l)):
    print('\n\nStep:',i+1,'--->',l)

    mini = i
    for j in range(i+1,len(l)):
        
        if l[j]<l[mini]:
            mini=j
    print(f"\n\t\tMinimum: {mini}")
    print(f'\t\tSwapping {mini} with {l[i]}(FOR INDEX-{i})')

    l[i],l[mini]=l[mini],l[i]
    print( '\n\t    ',l)

print('\n\nSorter List of no. is: \t',l)

