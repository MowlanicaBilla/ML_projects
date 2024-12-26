"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

def front_back(input_str):
    if len(input_str) == 1:
        return input_str
    else:
        return input_str[-1:] + input_str[1:-1] + input_str[:1]

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))