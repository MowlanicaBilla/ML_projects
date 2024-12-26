"""
Given three ints, a b c, one of them is small, one is medium and one is large. 
Return true if the three values are evenly spaced, so the difference between small 
and medium is the same as the difference between medium and large.


evenlySpaced(2, 4, 6) → true
evenlySpaced(4, 6, 2) → true
evenlySpaced(4, 6, 3) → false
"""


num_list = [2,4,6]
num_list_2 = [1,2,6]

def evenlySpaced(lst):
    return (lst[2]-lst[1] == lst[1] - lst[0])


print(evenlySpaced(num_list))
print(evenlySpaced(num_list_2))