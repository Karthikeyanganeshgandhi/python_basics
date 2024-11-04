# class parent:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def display_name(self):
#         print(self.fname,self.lname)
# class student(parent):
#     pass
# obj1=student("a","b")
# obj1.display_name()

# using super()
   
class parent:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display_name(self):
        print(self.fname,self.lname)
class student(parent):
   def __init__(self,fname,lname):
    super(). __init__(fname,lname)
    self.graduation=2024
x=student("a","b")
x.display_name()
print(x.graduation)


            
    