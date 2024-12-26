'''
Question:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''

# def max_subarray_sum_brute_force(nums):
#     # Handle edge case where nums is empty
#     if not nums:
#         return 0
    
#     n = len(nums)
#     max_sum = float('-inf')
    
#     # Iterate through each starting point of subarray
#     for i in range(n):
#         current_sum = 0
#         # Sum subarray starting from i to the end
#         for j in range(i, n):
#             current_sum += nums[j]
#             if current_sum > max_sum:
#                 max_sum = current_sum
    
#     return max_sum

# # Example usage
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_subarray_sum_brute_force(nums))  # Output: 6


# print(max(max_sum))

def max_subarray_sum(nums):
    # Handle edge case where nums is empty
    if not nums:
        return 0
    
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray_sum(nums))
