'''
Relationship is used to access the members of one class inside another class.
The advantage of relationships is code reusability.
There are two types of relationsships.
1. Has-A Relationship( also known as Composition)
2. IS-A Relationship( also known as Inheritance)
'''

#Examples:
'''
1. Employee HAS-A car
2. Employee IS-A Person
3. Car HAS-A Engine
4. Car IS-A Vehicle
'''

#1. HAS-A Relationship
'''
HAS-A Relationship is also known as Composition or Containership or Complex Objects.
In HAS-A Relationship we will build objects from smaller objects.
Ex: College is complex object and departments are smaller objects.

Here without College(Container Object) there are no departments(Contained objects).
'''

class Car:
    def __init__(self,cname,ccolor,cprice):
        self.cname=cname
        self.ccolor=ccolor
        self.cprice=cprice
    def Car_details(self):
        print(f'Car Name is {self.cname}')
        print(f'Car color is {self.ccolor}')
        print(f'Car Price is {self.cprice}')
        print("* " * 20)
        
class Laptop:
    def __init__(self,lname,lcolor,lprice):
        self.lname=lname
        self.lcolor=lcolor
        self.lprice=lprice
    def Laptop_details(self):
        print(f'Laptop Name is {self.lname}')
        print(f'Laptop color is {self.lcolor}')
        print(f'Laptop Price is {self.lprice}')

        
class Employee:
    def __init__(self,ename,eid,eaddress):
        self.ename=ename
        self.eid=eid
        self.eaddress=eaddress
        self.c=Car('Thar','Black','20Lakhs') # Object creation of car class
        self.l=Laptop("HP","White","40Thousand") # Object creation of Laptop class
    def Emp_details(self):
        print(f'Emp Name is {self.ename}')
        print(f'Emp id is {self.eid}')
        print(f'Emp Address is {self.eaddress}')
        print("* " * 20)
        self.c.Car_details() # Print the details of another class
        self.l.Laptop_details() # Print the details of another class
        

e=Employee("Ram", 1234, "Kakinada")
e.Emp_details()
        
'''
Emp Name is Ram
Emp id is 1234
Emp Address is Kakinada
Car Name is Thar
Car color is Black
Car Price is 20Lakhs
Laptop Name is HP
Laptop color is White
Laptop Price is 40Thousand
'''

#Here in the above program Employee is Containership, car and laptops are smaller objects