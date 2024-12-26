"""

Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""

def front3(input):
    return (input[0:3]*3 if len(input)>=3 else input)

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))