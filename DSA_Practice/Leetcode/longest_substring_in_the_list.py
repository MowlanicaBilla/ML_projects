"""
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
"""

import collections

letters = "abppplee"
words = {"able", "ale", "apple", "bale", "kangaroo"}

letter_position = collections.defaultdict(list)

# For each letter in 'letters', collect all the indices at which it appears.
# O(#letters) space and speed.
for index, letter in enumerate(letters):
    letter_position[letter].append(index)
        # For words, in descending order by length...
    # Bails out early on first matched word, and within word on
    # impossible letter/position combinations, but worst case is
    # O(#words # avg-len) * O(#letters / 26) time; constant space.
    # With some work, could be O(#W * avg-len) * log2(#letters/26)
    # But since binary search has more overhead
    # than simple iteration, log2(#letters) is about as 
    # expensive as simple iterations as long as 
    # the length of the arrays for each letter is
    # "small".  If letters are randomly present in the
    # search string, the log2 is about equal in speed to simple traversal
    # up to lengths of a few hundred characters.              
for word in sorted(words, key=lambda w: len(w), reverse=True):
    pos = 0
    for letter in word:
        if letter not in letter_position:
            break
    # Find any remaining valid positions in search string where this
    # # letter appears.  It would be better to do this with binary search,
    # but this is very Python-ic.
    possible_positions = [p for p in letter_position[letter] if p >= pos]
    if not possible_positions:
        break
    pos = possible_positions[0] + 1
    else:
    # We didn't break out of the loop, so all letters have valid positions  
        print(word)
