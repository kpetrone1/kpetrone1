# URL of Source: http://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/

"""
Session 16: Object-Oriented Programming: 
Classes and Functions | 27 Oct 2016
"""

import datetime

"""
1. Use the datetime module to write a program that 
gets the current date and prints the day of the week.
"""
# print(datetime.date())
# print(datetime.date(%m.%d.%Y))
# print(datetime.datetime.now())

# print(datetime.datetime.date(%m.%d.%Y))

# print(now.strftime('%m.%d.%Y'))

print(datetime.datetime.now())

print(strftime(%a)) ???

# print(datetime.today())

# print(date.fromtimestamp())


# print(datetime.time())
# print(date.today())


# print(datetime.date(), datetime.weekday())





"""
2. Write a program that takes a birthday as input and 
prints the user’s age and the number of days, hours, 
minutes and seconds until their next birthday.
"""

birthday = input("Please enter birthday: ")

print(age, ...)


"""
3.For two people born on different days, there is a day 
when one is twice as old as the other. That’s their 
Double Day. Write a program that takes two birthdays 
and computes their Double Day.
"""

"""
4. For a little more challenge, write the more general 
version that computes the day when one person is n times 
older than the other.
"""