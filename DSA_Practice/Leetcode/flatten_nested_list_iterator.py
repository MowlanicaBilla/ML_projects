# class NestedIterator(object):

#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#     def flatten(self, lst):
#         for el in lst:
#             if el.isInteger(): self.data.append(el.getInteger())
#             else: self.flatten(el.getList())

#     def next(self):
#         """
#         :rtype: int
#         """
        

#     def hasNext(self):
#         """
#         :rtype: bool
#         """


def flatten(lst):
    data = []
    for s in lst:
        if type(s) == list:
            data.append(s.isdigit())


lst = [[1,1],2,[1,1]]
print(flatten(lst))