def Val_parenthesis(s):
    d = {'(':')','[':']','{':'}'}
    stack = []
    for i in s:
        if i in d:  # 1
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:  # 2
            return False
    return len(stack) == 0 # 3


print(Val_parenthesis('()'))
print(Val_parenthesis('}{)('))