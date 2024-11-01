# decorators
# def my_decorate(fnc):
#     def inner():
#         print("i got decorated")
#         fnc()
#     return inner
# @my_decorate
# def ordinary():
#         print("iam ordinary")
# ordinary()

# def my_divide(func):
#     def inner(a,b):
#         print("iam, going to divide",a,"and",b)
#         if b==0:
#             print("whoops! cannot divide")
#             return
#         return func(a,b)
#     return inner
# @my_divide
# def divide(a,b):
#     print(a/b)

# divide(2,5)
# divide(2,0)

def my_frnds(bld):
    def inner():
        print("akash")
        bld()
    return inner
@my_frnds
def second_one(add):
    def inner():
        print("akash")
        add()
    return inner
@my_frnds
def third():
    print("karthik")
third()
    
    

       