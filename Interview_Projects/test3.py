# Distance array = [2, 2.5, 6, -1.8]

# Centroid = 0

# Index of the closest point to the centroid

import math

DISTANCE = [2, 2.5, 6, -1.8]
Centroid = 0

# Euclidean distance

def euclidean_distance(p1, p2):
    to_be_squared = abs(float(p1)-float(p2))
    squared_value = to_be_squared**2
    # print(squared_value)
    return math.sqrt(squared_value)
    # print(abs((float(p1)-float(p2))^2))
    # return math.sqrt(abs((float(p1)-float(p2))^2))

calculated_distance = []

for i in range(len(DISTANCE)):
    # calculated_distance[val] = euclidean_distance(Centroid, DISTANCE[ind])
    calculated_distance.append(euclidean_distance(Centroid, DISTANCE[i]))

# min_key = min(calculated_distance.values())
# print(calculated_distance.items(),)
# for i in range(len(DISTANCE)):
#     calculated_distance.append(math.sqrt((Centroid-DISTANCE[i])^2))

min_distance = min(calculated_distance)
print(calculated_distance.index(min_distance))

