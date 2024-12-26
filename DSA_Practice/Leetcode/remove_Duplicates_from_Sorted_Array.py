nums = [0,0,1,1,1,2,2,3,3,4]

# distinct_nums = list(set(nums))

# len_diff = len(nums) - len(distinct_nums)
# for i in range(len_diff):
#     distinct_nums.append(" ")

# print(distinct_nums)

# j = 0
# for i in range(1, len(nums)):
#     if nums[j] != nums[i]:
#         j=j+1
#         nums[j] = nums[i]
# print(j+1)

print(len(list(set(nums))))

# result = set(nums)
# if len(result) == len(nums):
#     print(len(nums))
# else:
#     r = list(result)
#     for i in range(len(nums) - len(result)):
#         r.append(1)
#     print(len(r))