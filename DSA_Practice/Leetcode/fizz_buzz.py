# FizzBuzz problem
# If number is divisible by 3 - print fizz
# if number is divisible by 5 - print buzz
# if number is divisible by 15 - print fizzbuzz
# else print the number

# Using if, else
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0: # if i%5 == 0 and i%3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Using dictionary
def fizzbuzz2(n):
    d = {3: 'fizz', 5 : 'buzz'}
    for i in range(1, n+1):
        result = ''
        for k,v in d.items():
            if i%k == 0:
                result += v
        if not result:
            result = i
        print(result)


print(fizzbuzz(20))
print(fizzbuzz2(20))

