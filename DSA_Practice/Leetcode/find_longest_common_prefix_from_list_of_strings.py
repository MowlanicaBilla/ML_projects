"""
Suppose we have a list of lowercase strings, we have to find the longest common prefix.

So, if the input is like ["antivirus", "anticlockwise", "antigravity"], then the output will be "anti"

To solve this, we will follow these steps −

sort the list words alphabetically

prefix := a new list
flag := 0
for i in range 0 to size of words[0], do
for each j in words, do
if j[i] is not same as last element of prefix, then
delete last element from prefix
flag := 1
come out from the loop
if flag is same as 1, then
come out from the loop
return string after concatenating all elements present in prefix array
Let us see the following implementation to get better understanding −
"""

class Solution:
    def solve(self, words):
        words.sort()
        prefix = []
        flag = 0
        for i in range(len(words[0])):
            prefix.append(words[0][i])
            for j in words:
                if j[i] != prefix[-1]:
                    prefix.pop()
                    flag = 1
                    break
            if flag == 1:
                break
        return ''.join(prefix)



ob = Solution()
words = ["antivirus", "anticlockwise", "antigravity"]
print(ob.solve(words))