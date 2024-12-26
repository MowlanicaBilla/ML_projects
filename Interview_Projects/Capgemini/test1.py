# Accept a number from the user and generate fibonacci series till that number
# 5
# 0, 1, 1, 2, 3

def fibonacci(n):
    for i in range(len(n)):
        if n<=0:
            print(n)
        elif n==1:
            print(n)
        else:
            print()
    # if n <= 0:
    #     return output_list
    # elif n == 1:
    #     output_list.append(0)
    #     output_list.append(1)
    #     return output_list
    # else:
    #     return fibonacci(n-1)
    
print(fibonacci(5))
