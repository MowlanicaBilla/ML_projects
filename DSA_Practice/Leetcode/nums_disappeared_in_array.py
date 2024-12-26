nums = [4,3,2,7,8,2,3,1]
op = []
for i in range(0, len(nums)):
    op.append(i + 1)
print(list(set(nums) ^ set(op)))
print(op)

# print(set(range(1, len(nums)+1)) - set(nums))

print(list(set(range(1, len(nums)+1))-set(nums)))