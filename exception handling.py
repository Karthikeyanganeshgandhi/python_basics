# try and except

# try:
#     numerator=10
#     denominator=0

#     result=numerator/denominator
#     print(result)

# except:
#     print("error : denominator can be 0")

# 2

# try:
#     even_numbers=[2,4,6,8]
#     print(even_numbers[5])

# except IndexError:
#     print("index out of bond")

# using string

# try:
#     text="hello world!"
#     char=text[20]

# except IndexError as e:
#     print(f"index error occured : {e}")

# else:

# try:
#     fruits=["apple","orange","cherry"]
#     print(fruits[2])

# except IndexError:
#     print("index out of bond")

# else:
#     print("successfully accessed the list elements")

# finally:

# try:
#     x=10
#     y=0
#     result=x/y

# except ZeroDivisionError:
#     print("cannot divide by zero")

# finally:
#     print("this block always runs")

try:
    fruits=["apple","banana","orange"]
    print(fruits[2])

except IndexError:
    print("index out of bond")

else:
    print("successfully accessed the list items")

finally:
    print("this block always run")