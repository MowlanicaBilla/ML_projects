a = [-1,3,2,0]
stack = []

def find132pattern(nums):
    stack = []
    s2 = float('-inf')
    print(s2)
    for i in nums[::-1]:
        print(i)
        if i<s2: 
            return True
        while stack and i>stack[-1]: 
            s2 = stack.pop()
        stack.append(i)
    return False




print(find132pattern(a))














# a = [-1,3,2,0]

# def find132pattern(nums):
#         for i in range(0,len(nums)-2):
#             val = nums[i:i+3]
#             print(val)
#             if val[0] < val[2] < val[1]:
#                 return True
#         return False

# print(find132pattern(a))