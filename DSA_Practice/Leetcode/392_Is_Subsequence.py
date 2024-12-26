"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

def is_subsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    start = 0
    for c in s:
        i = t.find(c, start)
        if i == -1:
            return False
        start = i + 1
    return True


print(is_subsequence(s = "abc", t = "ahbgdc"))
print(is_subsequence(s = "axc", t = "ahbgdc"))