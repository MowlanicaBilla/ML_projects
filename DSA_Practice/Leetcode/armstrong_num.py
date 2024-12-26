# Armstrong number
# A number that is equal to the sum of cubes of its digit
# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1+125+27 = 153



def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp%10
        sum += digit**3
        temp = temp//10

    if n == sum:
        print("Yes")
    else:
        print("No")
print(armstrong(153)) 


# Print armstrong numbers within a particular range

def armstrong_num(start, end):
    for n in range(start, end):
        sum = 0
        temp = n
        while temp > 0:
            digit = temp%10
            sum += digit**3
            temp = temp//10

        if n == sum:
            print(n)

print(armstrong_num(0, 500))

# Write sum of digits of a number
def sum_of_digits(n):
    sum = 0
    temp = n 
    if n>9:
        while temp > 0:
            digit = temp%10
            sum += digit**3
            temp = temp//10
    else:
        sum = n 
    return sum

print(sum_of_digits(143))