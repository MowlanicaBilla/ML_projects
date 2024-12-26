# Second highest number in a list
# Using for-loop
# Assuming the list will be mroe than 2 numbers

def second_highest_num(l):
    if l[0] > l[1]:
        first = l[0]
        second = l[1]
    else:
        first = l[1]
        second = l[0]
    
    for i in range(2, len(l)):
        if l[i] > first:
            second = first
            first = l[i]
        # elif l[i] > second: # if there are repeating numbers, this will output repeated num
        elif l[i] > second and first!= l[i]:
            second = l[i]

    return second

l = [10,20,30,4, 100, 666, 666]
print(second_highest_num(l))




# Using reverse sort
def second_highest_num_using_sort(l):
    l.sort(reverse=True)
    print(l[1])
    l.sort()
    print(l[-2])


# Finding the Nth highest
def second_highest_num_using_sort(l, n):
    l.sort(reverse=True)
    print(l[n-1])

# Using set and max(); not recommended
l = [10,20,30, 4,100, 22, 666,666, 2, 44, 20]
new_l = set(l)
print(new_l)
new_l.remove(max(new_l))
print(new_l)
print(max(new_l))
