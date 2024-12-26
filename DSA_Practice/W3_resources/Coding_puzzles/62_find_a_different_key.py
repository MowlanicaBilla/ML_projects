"""
62. Write a Python program to find the dictionary key whose case is different than all other keys.
Input:
{'red': '', 'GREEN': '', 'blue': 'orange'}
Output:
GREEN
Input:
{'RED': '', 'GREEN': '', 'orange': '#125GD'}
Output:
orange
"""


color_dict = {'red': '', 'GREEN': '', 'blue': 'orange'}
for different in color_dict:
    if all(k.islower() != different.islower() for k in color_dict if k != different):
            print(different)
    

