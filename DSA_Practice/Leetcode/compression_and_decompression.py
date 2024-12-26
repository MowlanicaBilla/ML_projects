"""
https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!

In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc

Other rules
Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

Characters allowed as input include digits, small English letters and brackets [ ].

Digits are only to represent amount of repetitions.

Letters are just letters.

Brackets are only part of syntax of writing repeated substring.

Input is always valid, so no need to check its validity.

Learning objectives
This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.
"""

"""
Solution explained, commentary
A basic solution involves use of simple recursion and loops.

Alternatively you can try a “peel the onion" approach, where you first decode top layer without using recursion, and then if there is any repetition group left, do the same with output after first phase. This is not bad, but the first approach is better as it may use a lot less memory.

There are several catches, for example:

numbers with multiple digits, like 10 or 100
handling non-repeated strings
handling repetitions inside
not doing the same job twice
not copying too much
Discussion questions
Once you've tried the problem, try thinking through these questions -- and maybe even write more code to push your skills a step further.

1. How would you test your solution in light of you've practiced in this path?

2. What are some different approaches you could take to your solution -- and how would you test those?
"""


string = "3[abc]4[ab]c"
# Expected output : abcabcabcababababc
# string = 'A3G3A'

expanded = ''

for character in string:
    if character.isdigit():
        expanded += expanded[-1] * (int(character) - 1)
    else:
        expanded += character

print(expanded)