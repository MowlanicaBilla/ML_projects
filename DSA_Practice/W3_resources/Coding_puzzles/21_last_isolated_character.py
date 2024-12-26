"""
21. Write a Python program to check, for each string in a given list, 
whether the last character is an isolated letter or not. Return True or False.
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]
"""
def last_isolated_character(input_list):
    return [len(s.split(" ")[-1])==1 for s in input_list]

strs =  ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Check, for each string in the said list, whether the last character is an isolated letter:")
print(last_isolated_character(strs))
strs =  ['ca t', 'car', 'fea r', 'cente r']
print("\nOriginal strings:")
print(strs)
print("Check, for each string in the said list, whether the last character is an isolated letter:")
print(last_isolated_character(strs))