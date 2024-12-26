"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""

# nums = [2,2,3,2]
# one, two = 0, 0
# for i in nums:
#     print(one ^ i, two | (one & i), two & i)
#     one, two, three = one ^ i, two | (one & i), two & i 
#     one, two = one & ~three, two & ~three
#     print(one, two)


nums = [2,2,3,2]

def singleNumber(nums):
    res = 0
    for i in range(32):
        count = 0
        for num in nums:
            count += (num >> i) & 1
        rem = count % 3
        if i == 31 and rem:
            res -= 1 << 31
        else:
            res |= rem * (1 << i)
    return res

print(singleNumber(nums=nums))