"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

# num = [2,7,11,15]
# target = 9
# num = [2,3,4]
# target = 6
numbers = [0,0,3,4]
target = 0


# ind_output = []

# for ind, val in enumerate(num[:-1]):
#     for val2 in num[ind:]:
#         print(ind, val, val2)
#         if val+val2 == target and val!=val2:
#             ind_output.append(num.index(val)+1)
#             ind_output.append(num.index(val2)+1)
#         elif val+val2 == target or val==0 or val2==0:
#             ind_output.append(num.index(val)+1)
#             ind_output.append(num.index(val2)+1)

def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while True:   
        if target > numbers[i] + numbers[j]:
            i += 1
        elif target < numbers[i] + numbers[j]:
            j -= 1
        else:
            return [i + 1, j + 1]    # you only get to this line once

print(twoSum(numbers=numbers, target=target))