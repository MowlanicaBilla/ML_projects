# In case of numbers:
# Using split method - converting number to string
# NOT PREFERRED

def palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False


def palindrome2(n):
    temp = n # 1456
    rev_num = 0
    while (temp>0):
        digit = temp % 10 # 6
        print(digit)
        rev_num = rev_num * 10 + digit
        # rev_num = 0*10 + 6 = 6
        temp = temp // 10 #145
    if n == rev_num:
        return True
    else:
        return False


n = 123454321
print(palindrome(n))