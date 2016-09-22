#2.3: Greatest Common Divisor
#Source: All code is from Joe James at https://www.youtube.com/watch?v=XVYb0Nin5K8.

def gcd(num1, num2):
    if num1>num2:                               #first, determine which number is smaller:
        num1, num2 = num2, num1                 #if num1 is greater than num2, swap the numbers so that num1 is always the smaller number (aka: assign num1 to always be the smaller of the two numbers)

    for x in range(num1,0,-1):                  #create a loop that ranges from num1 (the smaller of the two numbers) and counts down to 1, stepping down by 1 for each test (***the way the range function works: range (from, to +1, step) --> range from num1 to 1, stepping down by 1 each time***)
        if num1 % x == 0 and num2 % x == 0:     #if the remainder of num1 divided by x = 0 and the remainder of num2 divided by x = 0, then x is the gcf
            return x
    
num1 = 45
num2 = 65
print("Exercise 2.3:")
print("Solution to GCF: ", str(gcd(num1,num2)))

print("\n")

#2.4: Tower of Hanoi
#Source: All code is from Petros Sentis at https://www.youtube.com/watch?v=bGoxGlGiC_E.
#note: optimal solution to number of moves = (2^n)-1

print("Exercise 2.4:")
limit = 8                                       #limiting the number of disks for which we can solve the problem
#Solves the 'Tower of Hanoi' problem using recursion in order to move the disks from one rod to another

def move(n, start, dest, using):                #dest = desitnation, using = using peg
    if (n>1):
        move(n-1, start, using, dest)
        move(1, start, dest, using)             #1 = last disk = biggest disk
        move(n-1, using, dest, start)
    else:
        print(start, "->", dest)

#calls 'move' to start the computation of the recursive solution
def hanoi(h):                                   #h = height (number of disks)
    if (h<=0):
        print("Number of disks should be greater than zero.")
    elif(h>limit):
        print("Too many disks. (Maximum number of disks for this program is {}.)" .format(limit))
    else:
        print("List of Steps Required to Move", "\n", "All Disks to the Destination Peg:")
        move(h, "A", "C", "B")                  #specifying that we want to move h disks from Peg A (starting peg) to Peg C (destination peg) using Peg B for the transfer

hanoi(5)



