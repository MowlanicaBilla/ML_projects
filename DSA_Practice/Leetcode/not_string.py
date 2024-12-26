"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def not_string(input_str):
    if 'not' in input_str[:4]:
        return input_str
    else: 
        return 'not '+ input_str 



print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))