def factorial(n):
    if n == 1:              #ending point           #What does this mean?
        return 1
    result n * factorial(n-1)

print(factorial(1))
print(factorial(3))



###Do you not need "else" in the above function for the function to know to return n*factorial(n-1) if n does not =1? In other words, how does it kno wwhat to do if n does not =1?\