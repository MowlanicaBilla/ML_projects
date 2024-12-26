"""

The classic word-count algorithm: given an array of strings, return a Map<String, 
Integer> with a key for each different string, with the value the number of times 
that string appears in the array.


wordCount(["a", "b", "a", "c", "b"]) → {"a": 2, "b": 2, "c": 1}
wordCount(["c", "b", "a"]) → {"a": 1, "b": 1, "c": 1}
wordCount(["c", "c", "c", "c"]) → {"c": 4}
"""

def wordCount(input_list):
    word_count = {}
    for i in input_list:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count

print(wordCount(["a", "b", "a", "c", "b"]))
print(wordCount(["c", "b", "a"]))
print(wordCount(["c", "c", "c", "c"]))