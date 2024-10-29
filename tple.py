# change in tuple
# tple=("apple","banana","kiwi","pineapple")
# b=list(tple)
# b[2]="watermelon"
# d=tuple(b)
# print(d)

# hlo=("system","monster","cycle")
# b=list(hlo)
# b[1]="podaa"
# c=tuple(b)
# print(c)

# append
# thistuple=("apple","orange","kiwi")
# b=list(thistuple)
# b.append("pineapple")
# thistuple=tuple(b)
# print(thistuple)

# a=("banana","apple","kiwi")
# b=list(a)
# b.append("mango")
# thistuple=tuple(b)
# print(thistuple)

# +=
# thistuple=("apple","banana","kiwi")
# b=("pineapple" ,)
# thistuple += b
# print(thistuple)

# thistuple=("car","bike","auto","bus")
# c=("motor cycle" ,)
# thistuple += (c)
# print(thistuple)

# remove
# thistuple=("apple","banana","orange","kiwi")
# b=list(thistuple)
# b.remove("orange")
# print(b)

# delete
# thistuple=("apple","banana","orange")
# del thistuple
# print(thistuple)

# loop tuples
# thistuple=("apple","banana","kiwi")
# for x in thistuple:
#     print(x)

# a=("car","bike","auto")
# for x in a:
#     print(x)

# range()&len()
# b=("apple","banana","kiwi")
# for i in range(len(b)):
#     print(b[i])

# while 

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# a=("apple","orange","banana")
# i=1
# while i<len(a):
#     print(a[i])
#     i=i+1

# join tuples
# tuple=("a","b","c","d")
# tuple1=(1,2,3,4,5)
# tuple2=tuple+tuple1
# print(tuple2) 

# multyply tuples
a=("a","b","c","d")
b=(1,2,3,4)
c=a*2
d=b*2
print(c)
print(d)