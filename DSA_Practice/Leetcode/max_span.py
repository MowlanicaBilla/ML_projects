"""

Consider the leftmost and righmost appearances of some value in an array. 
We'll say that the "span" is the number of elements between the two inclusive.
A single value has a span of 1. Returns the largest span found in the given array. 
(Efficiency is not a priority.)


maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
"""

def maxSpan(input_list):
    span_dict = {}
    for i in range(len(input_list)):
        if input_list[i] not in span_dict:
            span_dict[input_list[i]] = [i, i]
        else:
            span_dict[input_list[i]][-1] = i

    spans = [(L[1] - L[0] + 1) for L in span_dict.values()]
    return max(spans)
print(maxSpan([1, 2, 1, 1, 3]))
print(maxSpan([1, 4, 2, 1, 4, 1, 4]))
print(maxSpan([1, 4, 2, 1, 4, 4, 4]))


