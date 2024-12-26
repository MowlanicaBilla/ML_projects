arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]

# duplicate_elements = []
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i] == arr[j]):    
#             duplicate_elements.append(arr[j]) 

# print(duplicate_elements)


# or

print(list(set([x for x in arr if arr.count(x) > 1])))