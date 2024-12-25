import math

N = math.floor(float(input()))

if N <= 0:
    print("N should be a positive number.")
else:
    for i in range(1, N + 1):
        print(i, end=" ")
