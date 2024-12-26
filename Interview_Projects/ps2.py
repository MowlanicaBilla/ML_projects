# Write a basic python program to find out a number-pair from a given list which sums upto a TARGET Value

nums = [1, 2, 3, 4, 5]
target = 3

# output = [1, 2]


def sum_to_target(nums, target):
    result = []
    p1, p2 = 0, len(nums)-1

    nums.sort()

    while p1<p2:
        if nums[p1] + nums[p2] < target:
            p1 += 1
        elif nums[p1] + nums[p2] > target:
            p2 -= 1
        else:
            result.append((nums[p1], nums[p2]))
            break
    return result


print(sum_to_target(nums, target))
