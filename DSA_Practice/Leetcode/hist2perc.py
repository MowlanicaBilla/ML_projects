import math
import numpy as np

hist = [10, 15, 4]
edges = [0.5, 6, 12, 25]
n_perc = 5
output = [0.5, 4.4875, 7.8, 10.7, 25]

index = np.linspace(0, 100, n_perc)
hist_output = np.histogram_bin_edges(hist, edges)
perc_numpy = [round(np.percentile(hist_output, i, interpolation='nearest'),1) for i in index]
print("Numpy percentile:", perc_numpy)

print("Output:", output)
# print("Hist:",hist_output)

# perc_numpy = [np.percentile(dist, i, interpolation='nearest') for i in index]

# def my_percentile(data, percentile):
#     n = len(data)
#     p = n * percentile / 100
#     if p.is_integer():
#         return sorted(data)[int(p)]
#     else:
#         return sorted(data)[int(math.ceil(p)) - 1]

# dist = np.random.randn(10000)




# perc_func = [my_percentile(dist, i) for i in index]
# print(perc_func)

# def calculate_percentile(arry, percentile):
#     size = len(arry)
#     return sorted(arry)[int(math.ceil((size * percentile) / 100)) - 1]

# perc_func = []
# for i in index:
#     perc_func.append(calculate_percentile(hist_output,i))



# # perc_func = [calculate_percentile(hist_output, i) for i in index]
# print(perc_func)