def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)-1, 0, -1):
        if (q[i] != i+1): # For first bribe
            if (q[i-1] == i+1):
                count += 1
                q[i], q[i-1] = q[i-1], q[i]
                # print("swap ->", q)
            elif (q[i-2] == i + 1): # For second bribe
                count += 2
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i-1], q[i] = q[i], q[i-1]
                # print("swap ->", q)
            else:
                print('Too chaotic')
                return
    print(count)