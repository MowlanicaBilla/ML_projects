"""
47. Write a Python program to Filter for the numbers in numbers in a given list 
whose sum of digits is > 0, where the first digit can be negative.
Input:
[11, -6, -103, -200]
Output:
[11, -103]
Input:
[1, 7, -4, 4, -9, 2]
Output:
[1, 7, 4, 2]
Input:
[10, -11, -71, -13, 14, -32]
Output:
[10, -13, 14]
"""

num_list = [11, -6, -103, -200, -40050]
for n in num_list:
    if int(str(n)[:2]) + sum(map(int, str(n)[2:])) > 0:
        print(n)


def filter_num_by_sum(nums):
    return [n for n in nums if int(str(n)[:2]) + sum(map(int, str(n)[2:])) > 0]
nums =  [11, -6, -103, -200]
print("Original list:")
print(nums)
print("Find the numbers in the said list whose sum of digits is >0, where the first digit can be negative:")
print(filter_num_by_sum(nums))
nums =  [1, 7, -4, 4, -9, 2]
print("\nOriginal list:")
print(nums)
print("Find the numbers in the said list whose sum of digits is >0, where the first digit can be negative:")
print(filter_num_by_sum(nums)) 
nums =  [10, -11, -71, -13, 14, -32]
print("\nOriginal list:")
print(nums)
print("Find the numbers in the said list whose sum of digits is >0, where the first digit can be negative:")
print(filter_num_by_sum(nums))