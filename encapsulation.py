# encapsulation

# public 
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name :", self.name)
#         print("age :", self.age)
# s=student("aswin",20)
# s.display()

# private

# class bankbalance:
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance
#     def __display__balance(self):
#         print("balance :", self.__balance)

# b=bankbalance(1055084,5000)
# b.__display__balance()

# protect
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def _display(self):
        print("name : ", self.name)
        print("age : ", self.age)

class student(person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self._roll_number=roll_number

    def display(self):
        self._display()
        print("roll number : ", self._roll_number)

s=student("aswin",20,8)
s.display()