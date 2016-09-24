#The following code is from asdfg098 at https://epequeno.wordpress.com/2011/01/04/solutions-7-3/.

def mysqrt(a):
    a = float(a)
    x = 10.0
    while True:
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

import math

print()



def layout(
    
    
    
    
    m):
    s = str(m)
    return s+' '*(14-len(s))

def printout():
    n = 1
    while n<10:
        n = float(n)
        foo = mysqrt(n)
        bar = math.sqrt(n)
        diff = abs(foo-bar)
        print (n),
        print (foo),
        print (bar),
        print (diff)
        n += 1
printout()





#Session 7: Iteration (Homework due 23 Sept 2016)

import math
a = 64

diff = abs(y-x)
def mysqrt(a):
    while True:
        print(x)
        y = (x + a/x) / 2
        if diff < epsilon:                            #(revised from "if x ==y" because "it is safer to use the built-in function abs to compute the absolute value, or magnitude, of the difference between" x and y)
            break
        x = y
mysqrt()

mysqrt(a)

def test_square_root():
    str(a, "     ", mysqrt(a), "     ", math.sqrt(a), "     ", diff)
test_square_root()

print(test_square_root())





