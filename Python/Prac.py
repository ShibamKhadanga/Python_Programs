#Change Capital to small and small to capital

def fun(s):
    K=len(s)
    p=" "
    for i in range(0,K):
        if (s[i].isupper()):
            p=p+s[i].lower()
        elif (s[i].islower()):
            p=p+s[i].upper()
        else:
            p=p+'#'
    print(p)
a=("ShibamKhadanga947@gmail.com")
fun(a)
