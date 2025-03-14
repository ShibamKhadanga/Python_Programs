'''Given an array of integers, find the longest subarray where the absolute difference
between any two elements is less than or equal to 1.


Example:-

a=[1,1,2,2,4,4,5,5,5]

There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5].
The maximum length subarray has 5 elements.'''


#                                          Let a = [4, 6, 5, 3, 3, 1].

#                                          l = Counter(a):
#                                          l becomes {4: 1, 6: 1, 5: 1, 3: 2, 1: 1}.
#                                          ma = 0


#                                          The loop iterates from i = 1 to i = 99.


#                                          i = 1:

#                                              l[1] = 1
#                                              l[2] = 0 (2 is not in l)
#                                              l[1] + l[2] = 1
#                                              ma becomes max(0, 1) = 1.


#                                          i = 2:

#                                              l[2] = 0
#                                              l[3] = 2
#                                              l[2] + l[3] = 2
#                                              ma becomes max(1, 2) = 2.


#                                          i = 3:

#                                              l[3] = 2
#                                              l[4] = 1
#                                              l[3] + l[4] = 3
#                                              ma becomes max(2, 3) = 3.


#                                          i = 4:

#                                              l[4] = 1
#                                              l[5] = 1
#                                              l[4] + l[5] = 2
#                                              ma remains 3.


#                                          i = 5:

#                                              l[5] = 1
#                                              l[6] = 1
#                                              l[5] + l[6] = 2
#                                              ma remains 3.


#                                          i = 6:

#                                              l[6] = 1
#                                              l[7] = 0
#                                              l[6] + l[7] = 1
#                                              ma remains 3.


# The rest of the iterations will not change ma because the counts will
# be 0 or 1, and the total of the two adjacent counts will not exceed 3.

# return ma:

# The function returns 3.
# Therefore, pickingNumbers([4, 6, 5, 3, 3, 1]) returns 3


from collections import Counter
def pickingNumbers(a):
    # Write your code here
    l=Counter(a)
    ma=0
    for i in range (1,100):
        ma=max(ma,l[i]+l[i+1])
    return ma
