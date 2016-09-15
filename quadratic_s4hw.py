def quad():
    from math import sqrt  #importing the square root function from the math library
    print("The following python code will solve for the two roots (one positive and one negative) of a quadratic equation.")
    print()
    
    a=int(input("Please input the first coefficient "))
    b=int(input("Please input the second coefficient "))
    c=int(input("Please input the third coefficient "))
    print()

    disc = b**2 - 4*a*c     #b^2 - 4ac; declaring a new variable to find out value of discriminate
    disc1 = sqrt(disc)                  #declaring another variable
    positive_root_solution = (-b + disc1)/(2*a)     #this is the value of the discriminant; making a new variable
    negative_root_solution = (-b - disc1)/(2*a)

    print("The positve root of the quadratic equation is {0}, and the negative value is {1}".format(positive,negative))

    print("Citation: The YouTube video titled 'basics of python - how to solve quadratic equations and find their roots' uploaded by the user 'Carl Saptarshi' was used in writing this code. Much of the code from Carl Saptarshi was copied.")

    input()
    