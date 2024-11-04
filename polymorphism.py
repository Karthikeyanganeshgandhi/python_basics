# two types- overloading & overriding

# overloading
# class calculation:
#     def add(self,a,b):
#         x=a+b
#         return x
#     def add(self,a,b,c):
#         x=a+b+c
#         return x
# obj1=calculation()
# print(obj1.add(10,20,30))
# print(obj1.add(10,20))

# overriding

class animal:
    def speak(self):
        return "animal_sounds"
class dog(animal):
        def speak(self):
            return "bark"
class cat(animal):
        def speak(self):
            return "meow"
class lion(animal):
     def speak(self):
          return "roar"
x=dog()
print(x.speak())
y=cat()
print(y.speak())
z=lion()
print(z.speak())
    
        