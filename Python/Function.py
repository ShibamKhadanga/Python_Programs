s="School12@com"
K=len(s)
m=len(s)
for i in range (0,K):
    if s[i].isupper():
        p=s[i].lower
        print(True,p)
    elif s[i].islower():
        q=s[i].upper
        print(True,q)
    else:
        r=m+'#'
        print(True,r)

