# Compress a string and add its number beside it aaabbbcc → a3b3c2

# Using for loop

def compress(s):
    n = len(s)
    new_str = ''
    count = 1
    for i in range(n -1): # Looping n-1 because next we are going to iterate till s+1 then we'll get an error
        if s[i] == s[i+1]:
            count += 1
        else:
            new_str = new_str + s[i] + str(count)
            # new_str += (s[i] + str(count))
            count = 1 # this will loop only till last but 1 string
    new_str = new_str + s[n-1] + str(count) # For adding the last string
    return new_str

s = 'aabbccaaaafffeiii'
print(compress(s))



# using while loop

def compress2(s):
    n = len(s)
    i = 0
    new_s = ''
    while (i < n-1):
        count = 1
        while (i < n-1 and s[i] == s[i+1]):
            count += 1
            i += 1
        i += 1
        new_s += (s[i-1] + str(count))
    return new_s


s = 'aabbccaaaafffeiii'
print(compress2(s))
