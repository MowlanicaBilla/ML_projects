"""

Return the number of times that the string "code" 
appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""

def count_code(input_str):
    counter = 0
    for _ in range(len(input_str)-3):
        if input_str[_] == "c" and input_str[_+1] == "o" and input_str[_+3] == "e":
            counter += 1
    return counter

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
 
