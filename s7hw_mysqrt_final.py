#23 Sept 2016 (Homework following Session 7)

#While a few adjustments have been made, the majority of the following code has been sourced from a blog titled "Random Thoughts" by Estevan Pequeno at https://epequeno.wordpress.com/2011/01/04/solutions-7-3/.

#function to test Newton's method vs. math.sqrt() to find square root
#Note: Newton's method is represented below as "mysqrt," and math.sqrt, I believe, is represented as "libmath_method."


import math

def mysqrt(n):
    a = float(n)
    x = n / 2                   #rough estimate
    i = 0
    while i < 10:
        y = (x + n/x) / 2       #Newton's method
        x = y
        i += 1
    return y

def libmath_method(n):
    a = float(n)
    return math.sqrt(n)

#This function has a mix of int, str and float, so there is a bit of conversion going on.

def test_square_root():
    for i in range(1,10):
        n = str(mysqrt(i))      #mysqrt() gets int and returns float. Change to str.
        l = str(libmath_method(i))      #libmath_method() gets int and returns float. Change to str.
        ab = abs(mysqrt(i)-libmath_method(i))   #out as int in as float, no str
        if (len(n) or len (l)) == 3:
            print(i, n, '          ', 1, '          ', ab)
        elif len(n) == 12:
            print(i, n, ' ', ab)
        else:
            print(i, n, l, ' ', ab)
test_square_root()