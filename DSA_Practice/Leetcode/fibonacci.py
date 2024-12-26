# Using while loop
def fibonacci(n):
    a, b = 0,1
    print(a)
    while (b<n):
        print(b)
        a, b = b, a+b
        # c  = a + b
        # a = b
        # b = c


# Using for loop
def fibonacci2(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a+b
            a = b
            b = c
            return c

# Using recursion; Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
