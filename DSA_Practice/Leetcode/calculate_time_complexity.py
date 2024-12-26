
def fname(n):
    counter = 0
    for j in range(n//2,n):
        print(j)
        while j*n/2 <= 2:
            print(True)
        #     k = 1
        #     while k <= n:
        #         counter += 1
        #         k *= 2
        #     j += 1
        # print(counter)

print(fname(n=10))