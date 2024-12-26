"""
55. Write a Python program to find the numbers that are greater than 10 and have odd first and last digits.
[1, 3, 79, 10, 4, 1, 39, 62]
Output:
[79, 39]
Input:
[11, 31, 77, 93, 48, 1, 57]
Output:
[11, 31, 77, 93, 57]
"""
num_list = [1, 3, 79, 10, 4, 1, 39, 62]
# result = []
# for i in num_list:
#     if i > 10:
#         if int(str(i)[0])%2!=0 and int(str(i)[-1])%2!=0:
#             result.append(i)

# print(result)

# or

def test(num_list):
    return [x for x in num_list if x > 10 and x % 10 % 2 and int(str(x)[0]) % 2]

# for x in num_list:
#     if x > 10 and x % 10 % 2 and int(str(x)[0]) % 2:
#         print(x)

            
print(test(num_list=num_list))