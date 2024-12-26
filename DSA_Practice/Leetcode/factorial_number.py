# Factorial number
# for loop
# 2nd case - 145! = 1! + 4! + 5! = 1+24+120 = 145
# print the number from 1 to 1 lakh where the summation of the factorial of each digit
# equals to the actual numebr
# for example;
# 145! = 1! + 4! + 5! = 1+24+120 = 145

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

# Sum of factorial
def sum_of_facto(n):
    temp = n 
    sum = 0
    while temp>0:
        digit = temp % 10
        temp = temp // 10
        facto = factorial(digit)
        sum += facto
    if sum == n:
        print('yes')
    else:
        print('no')

print(sum_of_facto(145))

# Print the list of numbers that follows the case within an interval
def sum_of_facto_within_a_range(start, end):
    for n in range(start, end):
        temp = n 
        sum = 0
        while temp>0:
            digit = temp % 10
            temp = temp // 10
            facto = factorial(digit)
            sum += facto
        if sum == n:
            print(n)
print(sum_of_facto_within_a_range(0,200000))