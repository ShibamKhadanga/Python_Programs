#NPTEL WEEK 2 PROGRAMMING ASSIGNMENT


'''Q1. Write a function intreverse(n) that takes as input a positive
integer n and returns the integer obtained by reversing the digits in n.'''


def intreverse(n):
  l = 0
  r = 0
  while n>0:
      l = n%10
      r = r*10+l
      n = n//10
  return(r)
print(intreverse(689))




'''Q2. Write a function matched(s) that takes as input a string s and checks
if the brackets "(" and ")" in s are matched: that is, every "(" has a
matching ")" after it and every ")" has a matching "(" before it. Your function
should ignore all other symbols that appear in s. Your function should return
True if s has matched brackets and False if it does not.


EXAMPLE:
>>> matched("zb%78")
True
>>> matched("(7)(a")
False
>>> matched("a)*(?")
False
>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True'''

def matched(s):
    c=0
    for i in s:
        if c==-1:
            return False
        if i == "(":
            c=c+1
        if i == ")":
            c=c-1
    if c==0:
        return True
    else:
        return False
s = "a)*(?"
print(matched(s))








'''Q3. Write a function sumprimes(l) that takes as input a list of integers l and
returns the sum of all the prime numbers in l.'''




def sumprimes(l):
    ps = 0
    for i in l:
        s = 0
        for j in range(1,i+1):
            if i%j == 0:
                s = s+1
        if s==2:
            ps = ps + i
    return(ps)

l = [1,13,2,19,5,7,8,5]
print(sumprimes(l))
