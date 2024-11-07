# module
# a file containing a set of functions
# def greeting(name):
#     print("hello,"+ name)

# python modules

# python math

# import math
# x=math.sqrt(100)
# print(x)

# import math
# x=math.sqrt(50)
# print(x)

# to find factorial

# n=int(input("enter your number : "))
# import math
# print(math.factorial(n))

# to find the details in math

# import math
# print(dir(math))

# python date

# import datetime
# x=datetime.datetime.now()
# print(x)

# to print year and day

# import datetime

# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%B"))

# month

# import datetime

# x=datetime.datetime(2016,6,1)
# print(x.strftime("%B"))

# random module

# seed()
# radint()
# randrange()
# shuffle()
# random()

# seed()
# import random
# random.seed(2)

# print(random.random())
# print(random.random())
# print(random.random())

# radint()

# import random
# print("random numbers :",random.randint(0,10))

# python calendar

import calendar
y=int(input("enter your year :"))
z=int(input("enter a month : "))

print(calendar.month(y,z))