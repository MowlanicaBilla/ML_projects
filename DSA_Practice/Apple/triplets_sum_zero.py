'''
Question:
You are given a list of integers, and you need to find all the unique triplets in the list which give the sum of zero.

Example:

plaintext
Copy code
Input: [-1, 0, 1, 2, -1, -4]
Output: [[-1, 0, 1], [-1, -1, 2]]
'''


# Starting with taking an empty list to store the list

# output_list = []
# input_list = [-1, 0, 1, 2, -1, -4]
# sum = 0

# def remove_duplicates(nested_list):
#     # Convert the nested list to a set of tuples
#     unique_elements = set(tuple(sorted(sublist)) for sublist in nested_list)
#     # Convert the set back to a list and sort it
#     unique_list = [sorted(list(sublist)) for sublist in unique_elements]
#     return unique_list

# # first iterating through each element in the array
# for i in range(len(input_list)):
#     for j in range(i+1, len(input_list)):
#         remaining_sum = sum - (input_list[i] + input_list[j])
#         if remaining_sum in input_list[j+1:]:
#             # print(input_list[i], input_list[j], remaining_sum)
#             output_list.append([input_list[i], input_list[j], remaining_sum])

# print(remove_duplicates(output_list))

#############################

# Optimised code

def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    return result

# Example usage
input_list = [-1, 0, 1, 2, -1, -4]
output = three_sum(input_list)
print(output)  # Output: [[-1, -1, 2], [-1, 0, 1]]
