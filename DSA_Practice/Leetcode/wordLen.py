"""
Given an array of strings, return a Map<String, Integer> containing a key for every 
different string in the array, and the value is that string's length.


wordLen(["a", "bb", "a", "bb"]) → {"bb": 2, "a": 1}
wordLen(["this", "and", "that", "and"]) → {"that": 4, "and": 3, "this": 4}
wordLen(["code", "code", "code", "bug"]) → {"code": 4, "bug": 3}
"""

def wordLen(input_list):
    wordcount = {}
    for i in input_list:
        # if i in wordcount:
        wordcount[i] = len(i)
        # #     wordcount[i] += 0
        # # else:
        #     wordcount[i] = len(i)
    return wordcount

print(wordLen(["a", "bb", "a", "bb"]))
print(wordLen(["this", "and", "that", "and"]))
print(wordLen(["code", "code", "code", "bug"]))