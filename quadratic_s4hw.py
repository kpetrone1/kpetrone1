def quad():
    from math import sqrt  #importing the square root function from the math library
    print("The following python code will solve for the two roots (one positive and one negative) of a quadratic equation:")
    print()
    
    a=int(input("Please enter first coefficient: "))
    b=int(input("Please enter second coefficient: "))
    c=int(input("Please enter third coefficient: "))
    print()

    disc = b**2 - 4*a*c     #b^2 - 4ac; declaring a new variable to find out value of discriminant
    disc1 = sqrt(disc)                  #declaring another variable
    positive_root_solution = (-b + disc1)/(2*a)     #this is the value of the discriminant; making a new variable
    negative_root_solution = (-b - disc1)/(2*a)

    print("The positve root of the quadratic equation is {0}, and the negative value is {1}".format(positive_root_solution,negative_root_solution))
quad()

print('\n')

print("Citation: The YouTube video titled 'basics of python - how to solve quadratic equations and find their roots' uploaded by the user 'Carl Saptarshi' was used in writing this code. Essentially all of the code for this assignment was taken directly from Carl Saptarshi. The URL for the video is: https://www.youtube.com/watch?v=RqvAfzjAG9s.")