def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    d = {i:x for i, x in zip(indices, s)}
    print(d)
    return ''.join([d[i] for i in sorted(indices)])


s = "aiohn"
indices = [3,1,4,2,0]

print(restoreString(s,indices))