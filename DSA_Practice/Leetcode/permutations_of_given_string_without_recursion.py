
# Python program to implement
# the above approach
def permute(s, answer):
    if (len(s) == 0):
        print(answer, end = "  ")
        return
     
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)
 
# Driver Code
answer = ""
# s = input("Enter the string : ")
s = "ABCD"
print("All possible strings are : ")
permute(s, answer)