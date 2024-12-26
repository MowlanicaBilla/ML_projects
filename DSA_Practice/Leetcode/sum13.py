"""

Return the sum of the numbers in the array, 
returning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

"""
from tkinter.tix import InputOnly


def sum13(input_list):
    i = 0
    sum = 0
    while i < len(input_list):
        if input_list[i] == 13:
            i +=1
        else:
            sum += input_list[i]
        i += 1
    return sum

# print(sum13(input_list=[1, 2, 2, 1, 13]))
# print(sum13([1, 2, 13, 2, 1, 13]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))
