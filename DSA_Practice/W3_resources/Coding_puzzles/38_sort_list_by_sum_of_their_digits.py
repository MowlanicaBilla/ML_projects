"""
38. Write a Python program to sort the numbers of a given list by the sum of their digits.
Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Output:
[10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
Input: [23, 2, 9, 34, 8, 9, 10, 74]
Output:
[10, 2, 23, 34, 8, 9, 9, 74]
"""

num_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def sort_list_by_sum(num_list):
    return sorted(num_list, key=lambda n: sum(int(c) for c in str(n) if c != "-"))


nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Original list of numbers:",nums)
print("Sort the numbers of the said list by the sum of their digits:")
print(sort_list_by_sum(nums))
nums = [23,2,9,34,8,9,10,74]
print("\nOriginal list of numbers:",nums)
print("Sort the numbers of the said list by the sum of their digits:")
print(sort_list_by_sum(nums))