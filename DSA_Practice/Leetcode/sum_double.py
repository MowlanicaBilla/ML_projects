"""
Given two int values, return their sum. Unless the two values are the same, 
then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""

def sum_double(n1, n2):
    if n1 == n2:
        return 4*(n1)
    else:
        return n1+n2
print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))