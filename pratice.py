########  What is comments ##########

'''
Comments are text in written in conde to explain it, which the interpreter 
ignore during the execution. Ther are useful for improving code readibility
and it is help to other easely understand code logic.

Ther are  2 type of comments supports python 

1.Single line comments  also know as in-line comments (indicates # symbol)
2.Multi line comments  also know as block comments (indicute 3 quatations) 

'''

###### What is variable ###########

'''
Variable is the name of address where data will be store in it
        Variable are containers for  stored a variable 

        we can create variable different ways 

                1. We can create one varible to assign one value   a = "mani"
                2.We can create one variable to assing multiple values  a = 10,20,30
                3.We can assing the one value to multiple variables a=b=c=20
                4.We can create multiple variable to assign multiple value in single line (a,b,c=10,20,30)

   Rules of variable creations

        1.Variable name must start with a latters and underscore character 
        2.A variable name cannot start with a number 
        3.A variable name can only contain alpha-Numeric characters and underscxres
        4.Variable names are case-sensitive
        5.The reserved words cannot be used naming the variable.
'''

######## What is data ############

'''Raw metarial of requried informatation ex: images, text, etc '''


####### What is globle Variable ###########

'''The variable we created out side of the funcation called global variable 
   global variable  we can access inside the funcation and out side the '''


########### What is data types ##########

'''
integr data type  ## int is denoted with int() funcation and the hole numbers are called intergers 
float data type    ## the desiminal nubers are called floate numbers we can denoted with float () funcation 
boolean data type # boolien is give output True or false 
complex data type 
string  ## "mani"

        list data type 
        set data type 
        tuple data type 
        dictonary data type 
'''

######### What is oprators ###########

'''

An operator in programming is a symbol or keyword that performs 
a specific operation on one or more operands (values or variables).
Operators are essential 
for performing calculations, comparisons, logical decisions, 
and more in code.

1.Arthemitical Operator (Arthimetical operators or +,-,*,/,//̣,%)
2.Comparisation Operator(Comparasition operators are >,<,<=,>=,==,!=) 
3.Logical operator (Logical operator is (and, or not ))
4.Assignment Operator (Assignment operators +=,-=,/=,*=,//=,%=)
5.Bitwisw operator ()
6.Membership operator (Membership operator are (in ,not in ))
7.Identify Operator (Identify Operator are (is ,is not ))

'''

####### What is control statement #########
'''
Control statements are 
1.Conditional statemnt (Conditional statements are (if, elif,else ))
2.Loping statemnets (Loping statements are (While, For ))
3.Transfar Statement (Transfar statements are (pass,continue,breake))

'''
######## What is List  ############

'''List is a collection of elaments with various data types. 
It is mutablle means we caan change the values after creation of list also
List with [] '''


###### What is Tuple #######
'''A tuple in python similir to list . The difference bitween the two is that we 
cannot change the elements of a tuple once it is assigned we can change the elements od a list 
Tuple with () '''


##### What is set #########

'''Set is a collection of elements with various datatypes. Set is mutable(we can change)
 and its elements are immutable(we can't change ). Set  cannot accept duplicate elements.Set cannot folliw Order 
   Set with {}  '''



###### What is funcation #########
'''Funcation is collection statements or a pieace of code to perform to a specific task'''
        # Advantages 
                # 1. Code Reusability
                # 2. Improve Modularity 


##### Types of funcations ##########
'''
1. Buils in funcation
2. User Defined Funcations.

  *** Build in Funcations -- This Funcations are already created by Python people 
        such type of funcation are called as predefin funcations or Build in funcations.

  *** User Defind Funcations -- These Funcations are created by users as per requirements.

'''


######### FILE HANDLING ###############

'''
File handling is an essantial concept and that allows to you read from and write to file.
Python provide built in funaction to access easy and effective way
'''

# s=open('sample.py' , mode='r')
# print(s.read())
# s.close()

# s=open('sample.py',mode='w')
# s.write('Hello Mani are you there')
# s.close()


# s=open('sample.py',mode='a')
# s.write("bye bye append")
# s.close()


# s=open('sample.py',mode='w+')
# print(s.read())
# s.write("r+ Mode")
# s.close()


# s=open('sample.py',mode='w+')
# print(s.tell())
# s.write('w+ mode')
# print(s.tell())
# s.write('mani')
# s.seek(0)
# print(s.tell())

# print(s.read())
# s.close()

# with open('sample.py','r') as file:
#     s=file.read()
#     print(s)

# with open('sample.py','w') as file:
#     file.write("Thisis writin usimg the 'with' statement.\n")
#     file.write("It will automatically close the file when done.")

# import os

# if os.path.exists('sample.py'):
#     with open('sample.py','r') as file:
#         print(file.read())
# else:
#     print("this file does not exist")



########## OOP #################

'''
Oops means object oriented programming opp is a programming paradaigram to write a programm effectiveli.
in oop we will develop mainly to using class andf object.oop is very sutable for large and complex application 
oop is follow the dry code apporach.
'''

# pop Calculation

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b == 0:
#         print("Error! Division by Zero")
#     else:
#         return a/b

# print(mul(10,15))

# oop Calculation

# class Calcilator:
#     def __init__(self,a,b):
#         self.a =a
#         self.b=b
#         self.result=0


#     def add(self):
#         self.result=self.a+self.b
#         return self.result
#     def sub(self):
#         self.result=self.a - self.b
#         return self.result
    
#     def mul(self):
#         self.result=self.a * self.b
#         return self.result
    
#     def div (self):
#         if self.b == 0 :
#             return "error"
#         else:
#             self.result=self.a / self.b
#             return self.result
# cla=Calcilator(10,0)

# print(cla.div())


######## Class And Object##########


# what is class
'''
Class is a blue print of object.it is logical entity and it is virtual and not a real.
if we want to create an object,then we requried a bule perint and that blue print 
is know as class .collection of object is know as Class.
Inside of the class we will represented properities and behaviours     
'''

# what is Object 
'''
Object is a real entity and it isa physical entity.Object is the interface of class.Objects are created inside the head memory
'''

# what is reference variable 

'''
Reference variable is used to refer to an object.Reference variable is acting as an accessor.
Reference variable is used to access properties and methods of an object.
'''


## Example: 1 

# class mani:
#     marks=10 # properitie
        # this is behaviour 
#     def sample(self): # self is the insede of the class reference variable
#         print("helo World")

# s=mani() # s is outside of the class reference variable 

# print(s.marks)
# s.sample()


##Example: 2

# class Student:
#     marks=10 
#     def sample(self,name,age):
#         print(f"my name is {name} and my age is {age}")
# s=Student()
# s.sample("mani",30)


# Example :3 

# class Student :
#     def __init__(self,name,age):  # constractor 

#         self.name =name 
#         self.age=age

#     def details(self):  # inside of the reference variable 

#         print(f"My name is {self.name} ans My age is {self.age}")

# s=Student("Mani",30)  # Out side of the class reference variable 
# s.details()


######### self variable ##########


'''
we can access attributes and methods inside the class.
These variables are used to access instace variables an dinside methods.
Self is used to refer to a current class object or current memory.
'''

# Reference Variable:
 
'''We can access object attributes and methods outside o fthe class '''

# Example 1






###### What is Inheritance ###########
'''Inheritance is a mechanism for creating a new class from an existing class.
Here the old class is called Basw class and the new class is called Derived class.'''


### What is Operator Overloading #####
'''
If we will use same operator in different purpose then it is called operator overloading
'''

### What is Method Overloading ########

'''If 2 or more methods have same name with different no of parameters od different types of 
 parameters is called method overloading
  Python does not support method overloading. Other language like java supports it
  But indirectly we can archieve method overloading by using multiple dispatch decorator
 '''

### What is Method Overloading ########

'''Operator overriding (also called as operator overloding ) is posible in python '''
### What is Method Overriding########
'''
A parent containg some method that method by default available to the child class
If child class wahnt, then child can provide own implementation for those methods,
 This mechianism is called as method overriding 
'''

####### What is constructor overloading ########
'''Constructure overloading is a mechaism in which a class can have any number of constructures
with different no of parameters of different type of paramaters.
Generally it doesnot support but we overcome withh multi dispatch module '''

####### What is constructor overriding ########
'''
Parent class constructure by default avalible to child class,If child class wont satisfy with parent class
then child class can override it
'''

### What is abstraction #########
'''Abstraction means hiding the implementation part and show functionality to the user, this process is called as abstraction.
By using abstract class and interface we can achieve abstraction.
By using interface, we can achieve 100% abstraction whereas by using abstract class we can achieve 0 to 100% abstraction.'''


##### what is interface ######
'''
If the class holds hold only abstract methods then it is know as interface.
Where abstract class  contain abstract as well as constreate method
Pythons doesnot provide any support for interface , so we want define by using abc module
'''