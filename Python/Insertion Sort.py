


''' .................................................Insertion Sort............................................... '''

# l = list(map(int, input("Enter Sace Separated Numbers: ").split()))
# l=[12,10,35,2,21,32]


print('Given List of no. is: \t',l)


for i in range(1,len(l)):
    print('\n\nStep:',i,'--->',l)
    
    for j in range (0,i):
        print('\n',l[i],'<',l[j],'is ', l[i]<l[j])
        
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
            
        print(l)
    print('\n')

print('Sorter List of no. is: \t',l)

