# https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-25.php
"""
Write a Python program to find the XOR of two given strings interpreted as binary numbers. 
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
"""
def xor_of_two_strings(lst):
    return bin(int(lst[0],2) ^ int(lst[1],2))

print(xor_of_two_strings(lst=['0001', '1011']))

