


''' .................................................Insertion Sort............................................... '''

# l = list(map(int, input("Enter Sace Separated Numbers: ").split()))

l=[12,10,35,2,21,32]


print('Given List of no. is: \t',l)


for i in range(1,len(l)):
    print('\n\nStep:',i,'--->',l)
    
    for j in range (0,i):
        print('\n\t',l[i],'<',l[j],'is ', l[i]<l[j])
        print('\t
              Swap',l[i],'with',l[j])
        
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
            
        print('\t',l)
    print('\n')

print('Sorter List of no. is: \t',l)

