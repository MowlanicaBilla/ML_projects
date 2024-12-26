def sum_of_positive_int(num):
    if num <= 0:
        return 0
    else:
        return num + sum_of_positive_int(num-2)
    
print(sum_of_positive_int(6))
print(sum_of_positive_int(8))