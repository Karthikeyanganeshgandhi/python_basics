# two types - __iter__ and __next__

# mytuple=("apple","banana","cherry")
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# myint=("car","train","bus","truck")
# b=iter(myint)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# iter using words
# word="pineapple"
# a=iter(word)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# class Squares:
#     def __init__(self,length):
#         self.length=length
#         self.current=0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current>=self.length:
#             raise StopIteration
        
#         self.current+=1
#         return self.current **2
    
# square_num=Squares(5)

# for sq in square_num:
#     print(sq)

# print(next(square_num)) 

class squares:
    def __init__(self,length):
        self.length=length
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>=self.length:
            raise StopIteration
        self.current+=2
        return self.current **3
square_num=squares(30)

for sq in square_num:
    print(sq)

print(next(square_num))
