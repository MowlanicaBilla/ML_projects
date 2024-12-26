"""

Remove duplicates in a string

collapseDuplicates("a") → "a"
collapseDuplicates("aa") → "a"
collapseDuplicates("abc") → "abc"

"""

def removeDuplicates(input_str):
    out_of_order = "".join(set(input_str))
    print(out_of_order)
    output_str = ""
    for s in input_str:
        if s in output_str:
            pass
        else:
            output_str += s
    print(output_str)

str="geeksforgeeks"
print(removeDuplicates(str))