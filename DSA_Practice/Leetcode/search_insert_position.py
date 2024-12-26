nums = [1,3,5,6]
target = 2
if target in nums:
    for index, val in enumerate(nums):
        if target == val:
            print(index)
else:
    nums.append(target)
    nums = sorted(nums)
    for index, val in enumerate(nums):
        if target == val:
            print(index)
    # for index, val in enumerate(nums):
    #     print(index, val)
    #     if val < target:
    #         nums.append(target)
    #         print("Index:", index + 1)
    #     elif val >= target:
    #         print("Enter")
    #         nums.insert(index+1, target)
    #         print(nums)
    #         break
    # for i in range(len(nums)):
    #     print(i, nums[i])
    #     if nums[i] > target:
    #         break
    #     d = nums[:i] + [target] + nums[i:]
    #     print(d)
    #     for index, val in enumerate(d):
    #         if target == val:
    #             print(index)

# Another effective solution

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             for i in range(len(nums)):
#                 if nums[i] == target:
#                     return i           
#         else:
#             for i in range(len(nums)):
#                 if nums[i] > target:
#                     return i
#                 elif nums[len(nums)-1] < target:
#                         return len(nums)