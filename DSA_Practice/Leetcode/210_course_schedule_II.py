"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

"""

from collections import * 
class Solution:
    def findOrder(self, numCourses, prerequisites):                             
        pre, suc = defaultdict(int), defaultdict(list)         # declare dictionary, pre with int values and suc with list as values.
        for a, b in prerequisites:                             # iterate through prerequisites to map preres and successors of each courses.
            pre[a] += 1                                        # pre holds no of pre reqs for each course
            suc[b].append(a)                                   # suc holds successor of each course in lists
        free = set(range(numCourses)) - set(pre)               # In free you will get set of courses which doesnt have prereqs
        out = []                                               # variable to hold sequence of courses
        while free:                                            # if there is a course with out pre-reqs 
            a = free.pop()                                     # pop it
            out.append(a)                                      # append to sequence
            for b in suc[a]:                                   # Iterate through the successors of free course 
                pre[b] -= 1                                    # As this course is done decrement value of pre where this course was prereq
                pre[b] or free.add(b)                          # check if particular course has no more pre-reqs then add it to free
        # return out * (len(out) == numCourses)  or                # return sequence if all the courses are finished else empty array.
        if len(out) != numCourses:
            return []
        return out

s = Solution()
print(s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))