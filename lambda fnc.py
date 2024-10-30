# lambda/anonymous function

# x=lambda a:a+30
# print(x(5))

# a=lambda x,y:x*y
# print(a(10,5))

# call the lambda
# greet=lambda:print("hello world")
# greet()

# filter()
# def check_even(number):
#     if number%2==0:
#         return True
#     return False
# numbers=[1,2,3,4,5,6,7,8,9,10]
# find_even=filter(check_even,numbers)
# print(find_even)
# ans=list(find_even)
# print(ans)

# map ()
# numbers=[5,6,7,8]
# def square(number):
#     return number*number
# squared_numbers=map(square,numbers)
# result=list(squared_numbers)
# print(result)

# reduce()
# list1=[1,2,3,4,5]
# from functools import reduce
# product=reduce(lambda x,y:x*y,list1)
# print(product)