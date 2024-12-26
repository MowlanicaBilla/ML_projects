"""
Given a string, return the sum of the numbers appearing in the string, 
ignoring all other characters. A number is a series of 1 or more digit chars in a row. 
(Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. 
Integer.parseInt(string) converts a string to an int.)


sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
"""
import re
def sumNumbers(input_str):
    num_list = [int(num) for num in re.findall(r"\d+", input_str)]
    return sum(num_list)


print(sumNumbers("abc123xyz"))
print(sumNumbers("aa11b33"))
print(sumNumbers("7 11"))