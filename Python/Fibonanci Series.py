#Fibonanci series
a = 0
b = 1
c = 0
print(a,end=' ')
print(b,end=' ')
while c<100:
    c = a+b
    print(c,end=' ')
    a = b
    b = c
    
