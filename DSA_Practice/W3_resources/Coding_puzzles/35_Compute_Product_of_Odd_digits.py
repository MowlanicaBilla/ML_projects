"""
35. Write a Python program to compute the product of the odd digits in a given number, 
or 0 if there aren't any.
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945
"""

num = 123456789
flag = 1
for i in str(num):
    if int(i)%2 != 0:
        flag *= int(i)
print(flag)


