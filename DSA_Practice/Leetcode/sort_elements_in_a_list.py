# import random
# rand_list=[]
# n=10
# for i in range(n):
#     rand_list.append(random.randint(1,100))
# print(rand_list)

rand_list = [54, 23, 85, 73, 7, 5, 52, 88, 39, 71]
rand_list.sort(reverse=True)
print("Using in-built sort function:", rand_list)



# Without in-built function
new_list = []
while rand_list:
    minimum = rand_list[0]
    for val in rand_list:
        if val > minimum:
            minimum = val
    new_list.append(minimum)
    rand_list.remove(minimum)
print(new_list)