"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

"""
1. Take an empty dictionary
2. Loop through the given array
3. Sort each word in the dictionary while looping through the dictionary 
and checking if the sorted word is present in the dictionary.
4. If not, add the word to the dictionary and consider the sorted word as the key and word as the value, 
if yes, append the word to the value of the sorted array.  
5. Loop through the dictionary and print the values in the dictionary
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sortedword = "".join(sorted(word))
        
            if sortedword not in dict:
                dict[sortedword] = [word]
            else:
                dict[sortedword].append(word)
                
        result = []
        for item in dict.values():
            result.append(item)
        return result

