# CHaracter occurence
# 1. Least repeating character in a string
# 2. Count of any particular element
# 3. Count of all elements



# Least character occurence

def least_char_occurence(s):
    print(s)
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print(ch) # To print all the occurences of a character
    result = min(ch, key= ch.get)
    print(result)

s = "aaabbbhhhshhhhhssssjjijsjshdk"
print(least_char_occurence(s))


# Using in-built function counter; not preferred
from collections import Counter
s = "aabccdeessddw"
ch = Counter(s)
result1 = min(ch, key=ch.get)
print(result1)


# Count of any particular element; not preferred
# Uing count(for string, number, list)
l = [1,2,3,4,5,4,3,2,4,5,6,7]
print(l.count(4))

s = "aabccdeessddaaaaw"
print(s.count('a'))


# Without using in-built count / using dict
def count_char_occurence(s, search_ch):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] =  ch[i] + 1
        else:
            ch[i] = 1
    print(ch)
    try:
        print(ch[search_ch])
    except:
        print("Value not present") 

s = "aabccdeesaasddaaaaaaw"
print(count_char_occurence(s,'m'))



# Count all the occurences
def all_char_occurence(s):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] =  ch[i] + 1
        else:
            ch[i] = 1
    print(ch)


s = "aabccdeesaasddaaaaaaw"
print(all_char_occurence(s))