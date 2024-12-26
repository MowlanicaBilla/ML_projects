# By using split method
def palindrome(s):
    temp = s[::-1]
    if s == temp:
        return "Yes.!! It's a palindrome.!"
    else:
        return "No.!! It's not a palindrome.!"


# By using indexing / for loop
def palindrome2(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
        return True



# By using in-built reversed method
def palindrome3(input_string):
    rev_string = "".join(reversed(input_string))
    if input_string == rev_string:
        return True
    return False

# Using while-loop
def palindrome4(s):
    n = len(s)
    first = 0
    last = n-1
    while(first<last):
        if s[first] == s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True


s = "madam"
print(palindrome(s))
print(palindrome2(s))
print(palindrome3(s))
print(palindrome4(s))