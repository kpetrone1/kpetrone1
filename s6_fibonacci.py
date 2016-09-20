def fib(n):
    if n == 1 or n == 2:        #how can n equal two different numbers (1 and 2?)?

        return 1
    return fib(n-1) + fib(n-2)

    print(fib(3))

    print(fib(10))