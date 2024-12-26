# # def sum_list(lst):
# #     # l = [item for sublist in lst for item in sublist]
# #     result = []
# #     for sublist in lst:
# #         for item in sublist:
# #             result.append(item)
# #     # print(result)
# #     if len(result) == 1:
# #         return result[0]
# #     else:
# #         return result[0] + sum_list(result[1:])
    
# # print(sum_list([1, 2, [3,4], [5,6]]))


# def flatten(nasted_list):
#     """
#     input: nasted_list - this contain any number of nested lists.
#     ------------------------
#     output: list_of_lists - one list contain all the items.
#     """

#     # list_of_lists = []
#     # for item in nasted_list:
#     #     list_of_lists.extend(item)
#     # return list_of_lists
#     l = [item for sublist in nasted_list for item in sublist]
#     return l

# test1 = flatten([[1,2,3],[4,5,6]])
# print(test1)

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))