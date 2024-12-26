"""

Given an array of non-empty strings, create and return a Map<String, String> as follows: for each string add its first character as a key with its last character as the value.


pairs(["code", "bug"]) → {"b": "g", "c": "e"}
pairs(["man", "moon", "main"]) → {"m": "n"}
pairs(["man", "moon", "good", "night"]) → {"g": "d", "m": "n", "n": "t"}
"""

input_list = ["code", "bug"]

def pairs(input_list):
    output_dict = {}
    for i in input_list:
        output_dict[i[0]] = i[-1]
        
    return output_dict


print(pairs(["code", "bug"]))
print(pairs(["man", "moon", "main"]))
print(pairs(["man", "moon", "good", "night"]))