# Prime number
# 1. TO check if the number is a prime number or not

# Using flag
def prime_num(n):
    flag = False
    if n>1:
        for i in range(2, n//2+1): # Instead of looking for numebrs till n; nums that divide by 2 will not be a prime
            if n%i == 0:
                flag = True
                break
    if flag:
        return "It's not a prime"
    else:
        return "It's a prime"

print(prime_num(15))

# Using for-else:
def prime_number(n):
    if n > 1:
        for i in range(2, n//2 +1):
            if n%i == 0:
                print("No.! It's not a prime.!")
                break
        else:
            print("Yes.! It's a prime number")
    else:
        print("No.! it's not a prime")


# Print all the numbers in range
for i in range(100, 200):
    if all(i%num!=0 for num in range(2, i)):
        print(i)


def prime_range(start, end):
    for n in range(start, end):
        if n > 1:
            for i in range(2, n//2 +1):
                if n%i == 0:
                    break
            else:
                print(n)

print(prime_range(3, 10))