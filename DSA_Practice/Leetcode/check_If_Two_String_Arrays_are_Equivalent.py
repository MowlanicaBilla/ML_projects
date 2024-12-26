word1 = ["a", "cb"]
word2 = ["ab", "c"]

# w1 = w2 = ""
# for ind1, val1 in enumerate(word1):
#     w1 = w1 + val1
# for ind2, val2 in enumerate(word2):
#     w2 = w2 + val2
# if w1 == w2:
#     print("True")
# else:
#     print("False")


a = b = ""
for i in word1:
    a = a + i 
    print(a)
for i in word2:
    b = b + i 
if a == b:
    print('true')
else:
    print("False")