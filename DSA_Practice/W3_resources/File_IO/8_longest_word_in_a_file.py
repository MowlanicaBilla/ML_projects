with open('./Input/words1.txt') as f:
    words = f.read().split()
    maxlen = len(max(words, key=len))
    print(maxlen)
    print([word for word in words if len(word) == maxlen])