"""

Given a non-empty array, return true if there is a place to split the array 
so that the sum of the numbers on one side is equal to the sum of the numbers 
on the other side.


canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true
"""
input_list = [1, 1, 1, 2, 1]

def canBalance(input_list):
    output_list = []
    for i in range(len(input_list)):
        output_list.append(sum(input_list[0:i]) == sum(input_list[i:]))
    return any(output_list)== True

print(canBalance([1, 1, 1, 2, 1]))
print(canBalance([2, 1, 1, 2, 1]))
print(canBalance([10, 10]))