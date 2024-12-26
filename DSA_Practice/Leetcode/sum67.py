"""
Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending 
to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""

def sum67(input_list):
    sum = 0
    isBetween = False
    for i in range(len(input_list)):
        if input_list[i] == 6:
            isBetween = True
        if not isBetween:
            sum += input_list[i]
        if input_list[i] is 7 and isBetween:
            isBetween = False
    return sum

print(sum67(input_list=[1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))