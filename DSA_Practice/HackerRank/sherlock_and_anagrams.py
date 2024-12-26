from collections import Counter

def sherlockAnagrams(s):
    count = 0
    count_dict = Counter(s)
    for i in range(2, len(s)):
        sb = s[0:i]
        l = len(sb)
        count_dict["".join(sorted(sb))] += 1
        for j in range(1, len(s)):
            if j+l <= len(s):
                count_dict["".join(sorted(s[j:j+l]))] += 1

    print(count_dict)
    for key, val in count_dict.items():
        count += val*(val-1)//2

    return count


print(sherlockAnagrams("abba"))