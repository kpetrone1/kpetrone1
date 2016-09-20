age = int(input('How old are you?'))
if age >=21:
    print('Your age is ', age)
    #print('Your age is ' +str(age)+ '.')       #other way to print age
    #print('Your age is {}.' .format(age))      #other way to print age
    print('Yes, you can.')
elif age >=6:
    print('Your age is ', age)
    print('You are a teenager. No, you cannot.')
else:
    print('Your age is ', age)
    print('No, not allowed.')



#Nested
x = 1
y = 2
if x == y:
    print('x and y are equal.')
    else:
        if x < y: print ('x is less than y')
        else: print('x is greater than y')

#TO COMPLETE#
#Exercise 1
#Create a BMI calculator using if/elif.

weight = float(input(weight))
height = float(input(height))

def BMI_USA() = 703*(weight/(height**2))
    weight=float(input('Weight: '))
    height=float(input('Height: '))
def BMI_metric = weight/(height**2)

if BMI_USA =< 18.5:
    print('Underweight')
    else:
        if BMI_USA <=24.9
        print('Normal weight')
            else:
                if BMI_USA <=29.9
                print('Overweight')
                    else:
                        print('Obsese')

#Recursion
def countdown(n):
    if 



def print_n(s, n):
    if n <=0:
        return
        print(s)
        print('n = ', n)
        print_n(s, n-1)

print_n('Hello', 3)

