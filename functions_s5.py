#Exercise 2.4
import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference/n
    polygon(t, n, length)

def circle(t, r):
    circumference = 2 * math.pi * r
    n=int(circumference/3) + 1      #? Why divide by 3 and add 1?
    length = circumference/n
    polygon(t,n,length)             #? What does "t" stand for?

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length /3) + 1
    step_length = arc_length / n
    step_angle = angle/n
    
    for i in range(n):              #? in general, what does this do? also what is the range of values that composes n? how does a single character (aka n) represent a whole range of numbers? don't you need at least two characters (the max and the min)?
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t,n,length,angle)

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle/360
    n=int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n,step_length,step_angle)

def circle(t,n)
    arc(t,r,360)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and angle (in degrees) between them. t is a turtle."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
#Exercise 3
#Flower Illustration
print("Note: All of the code below has been copied verbatim from Allen Downey at the URL http://greenteapress.com/thinkpython2/code/polygon.py.")

import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments.
    
    t: Turtle object
    n: number of line segments
    length: length of each segments
    angle: degrees between segments
    """

    for i in rang(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """                 #What do the three sets of quotation marks achieve?

angle = 360.0/n
polyline(t, n, length, angle)

def arc(t,r,angle)
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """

    arc_length = 2 * math.pi * r * abs(angle)/360
    n = int(arc_length/ 4) + 1 #? Why divide by 4 and add 1?
    step_length = arc_length / n
    step_angle = float(angle)/n
    
    #making a slight left turn before starting reduces the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t,r)
    """Draws a circle with the given radius.

    t:Turtle
    r: radius
    """
    arc(t,r,360)

#the following condition checks whether we are running as a script, in which case run the test code, or being imported, in which case don't.

if__name__ == '__main__':
    bob = turtle.Turtle()

    #draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    #wait for the user to close the window
    turtle.mainloop()


#YingYang
print("Note: All of the code below has been copied verbatim from the URL https://svn.python.org/projects/python/tags/r32/Lib/turtledemo/yinyang.py.")

from turtle import *

def yin(radius, color1, color2):
        width(3)
        color("black", color1)
        begin_fill()
        circle(radius/2., 180)
        circle(radius, 180)
        left(180)
        circle(-radius/2., 180)
        end_fill()
        left(90)
        up()
        forward(radius*0.35)
        right(90)
        down()
        color(color1, color2)
        begin_fill()
        circle(radius*0.15)
        end_fill()
        left(90)
        up()
        backward(radius*0.35)
        down()
        left(90)

def main():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"

if__name__ == '__main__':
    main()
    mainloop()