'''
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))

print(gcd(a,b))
'''

#2.3: Greatest Common Divisor
#Source: Joe James at https://www.youtube.com/watch?v=XVYb0Nin5K8

def gcf(num1, num2):
    #num1 = int(input('Enter first number: '))        #??? What is another way to ask for an input?
    #num2 = int(input('Enter second number: '))
    if num1>num2:                               #first, determine which number is smaller:
        num1, num2 = num2, num1                 #if num1 is greater than num2, swap the numbers so that num1 is always the smaller number (aka: assign num1 to always be the smaller of the two numbers)

    for x in range(num1,0,-1):                      #create a loop that ranges from num1 (the smaller of the two numbers) and counts down to 1, stepping down by 1 for each test (***the way the range function works: range (from, to +1, step) --> range from num1 to 1, stepping down by 1 each time***)
        if num1 % x == 0 and num2 % x == 0:     #if the remainder of num1 divided by x = 0 and the remainder of num2 divided by x = 0, then x is the gcf
            return x
    
num1 = 45                                              #???How else can I define num1 and num2?
num2 = 65 
print(str(gcf(num1,num2)))



#2.4: Tower of Hanoi
#Source: All code is from Petros Sentis at https://www.youtube.com/watch?v=bGoxGlGiC_E.
#note: optimal solution to number of moves = (2^n)-1

limit = 8                                       #limiting the number of disks for which we can solve the problem
#Solves the 'Tower of Hanoi' problem using recursion in order to move the disks from one rod to another

def move(n, start, dest, using):                #dest = desitnation, using = using peg
    if (n>1):
        move(n-1, start, using, dest)
        move(1, start, dest, using)             #1 = last disk = biggest disk
        move(n-1, using, dest, start)
    else:
        print("Exercise 2.4:")                                                                                                                                  #??? Why is this printed repeatedly when the code is run?
        print("Because there is only one disk, there is only one step to move the disk from the first peg to the third peg. The step is listed below.")         #??? Is it correct to say that there is only one disk? Or could it be any number of disks where n>1????
        print(start, "->", dest)

#calls 'move' to start the computation of the recursive solution
def hanoi(h):                                   #h = height (number of disks)
    if (h<=0):
        print("Number of disks should be greater than zero.")
    elif(h>limit):
        print("Too many disks.", "\n", "Maximum number of disks for this program is {}." .format(limit))            #???How to remove the indentation in front of the line beginning with "Maximum number of disks"? <--solution: remove commas
    else:
        move(h, "A", "C", "B")                  #specifying that we want to move h disks from Peg A (starting peg) to Peg C (destination peg) using Peg B for the transfer

hanoi(5)

