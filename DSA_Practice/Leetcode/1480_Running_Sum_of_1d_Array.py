"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""

nums = [1,2,3,4]
output = []
flag = 0
for i in nums:
    flag += i
    output.append(flag)

print(output)


# Another approach
def runningSum(self, nums):
    i = 1
    while i<len(nums):
        nums[i]+=nums[i-1]
        i+=1
    return nums

# Without modifying the initial array

# Time O(N)
# Space O(1)

def runningSum(self, nums):
    res = [nums[0]] + [0] * (len(nums) - 1)
    for i, num in enumerate(nums[1:]):
        res[i + 1] += res[i] + num
    return res