"""

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""

def makes10(n1, n2):
    return (n1+n2 == 10 or n1 == 10 or n2 == 10)

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))