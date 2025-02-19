#self_variable:
'''
We can access attributes and methods inside the class.
These variables are used to access instance variables and instance methods.
self is used to refer to a current class object or current memory.
'''

#reference_variable:
'''We can access object attributes and methods outside of the class'''

#Example
class Student:
    def __init__(self,name,age):   #Constructor with self
        self.n=name
        self.a=age
    def details(self):
        print(f"My name is {self.n} and my age is {self.a}")
        
s1=Student("gopal",30)  #Here s1 is reference variable
s1.details()

#Example: Values at run time
class Student:
    def __init__(self):
        print(id(self))
        self.n=input("Enter your name:")
        self.a=int(input("Enter your age:"))
    def details(self):
        print(f"My name is {self.n} and my age is {self.a}")
        
s1=Student()
s1.details()

#Both self and reference variable pointing to same location it returns same address
class student():
    def __init__(self):
        print(id(self))
        
s1=student()
print(id(s1))

#Example: we can use x or anything instead of self variable
class Student:
    def __init__(x,name,age):   #Constructor with self
        x.n=name
        x.a=age
    def details(x):
        print(f"My name is {x.n} and my age is {x.a}")
        
s1=Student("gopal",30)  #Here s1 is reference variable
s1.details()