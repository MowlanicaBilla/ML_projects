"""
56. Write a Python program to find an integer exponent x such that a^x = n. Go to the editor
Input:
a = 2 : n = 1024
Output:
10
Input:
a = 3 : n = 81
Output:
4
Input:
a = 3 : n = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
Output:
170
"""


def integer_Exponent(n,a):
    m = 1
    x = 0
    while m != n:
        x += 1
        m *= a
    return x

