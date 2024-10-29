# thisset={"apple","banana","cherry"}
# print(thisset)

# duplicates not allowed
# thisset={"apple","orange","apple"}
# print(thisset)

# true & 1 are the same value
# thisset={"apple","banana","cherry",True,1,2}
# print(thisset)

# false & 0 are same
# thisset={"apple","banana",False,True,0}
# print(thisset)

# length
# thisset={"apple","banana"}
# print(len(thisset))

# set items
# set1={"apple","banana","cherry"}
# set2={1,3,2,6,5,4}
# set3={True,False,True,False}
# print(set1)
# print(set2)
# print(set3)

# type
# thisset={"apple","banana","cherry"}
# print(type(thisset))

# for x in set
# thisset={"apple","banana","cherry"}
# for x in thisset:
#     print(x)

# in
# thisset={"apple","banana","cherry"}
# print("apple" in thisset)

# not in
# thisset={"apple","banana","cherry"}
# print("pineapple" not in thisset)

# thisset={"apple","banana","cherry"}
# thisset.add("kiwi")
# print(thisset)

# thisset={"apple","banana","cherry"}
# makan={"cat","dog","puppy"}
# thisset.update(makan)
# print(thisset)

# thisset={"apple","banana","cherry"}
# thisset.remove("apple")
# print(thisset)

# thisset={"apple","banana","cherry"}
# thisset.discard("apple")
# print(thisset)

# thisset={"apple","banana","cherry"}
# x=thisset.pop()
# print(x)
# print(thisset)

# thisset={"apple","banana","cherry"}
# thisset.clear()
# print(thisset)

# thisset={"apple","banana","cherry"}
# del thisset
# print(thisset)

# thisset={"apple","banana","cherry"}
# for x in thisset:
#     print(x)

# join union()
# a={"a","b","c"}
# b={1,2,3,4}
# c=a.union(b)
# print(c)

# union can be represent as |
# a={'a',"b","c"}
# b={1,2,3,4}
# c=a | b
# print(c)

# set1={1,2,3,4}
# set2={"a","b","c","d"}
# set3={"akash","aswin"}
# set4=set1 | set2 | set3
# print(set4)

# join a set and tuple
# x={"a","b","c","d"}
# b=(1,2,3,4)
# z=x.union(b)
# print(z)

# set1={"a","b","c","d"}
# set2={1,2,3,4}
# set1.update(set2)
# print(set1)

# set1={"a","b","c"}
# set2=(1,2,3)
# set1.update(set2)
# print(set1)

# intersection()
# set1={"a","b","c"}
# set2={"car","bike","a"}
# set3=set1.intersection(set2)
# set4=set2.intersection(set1)
# print(set3 , set4)

# & - to join two sets
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)

# difference
# a={"apple","banana","mouse"}
# b={"microsoft","windows","mouse"}
# set1=a.difference(b)
# print(set1)

# a={"apple","banana","mouse"}
# b={"microsoft","windows","mouse"}
# set1= a-b
# print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)