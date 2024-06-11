Instance Method:
class student:   #class is keyword and student is class name
    school = "Telusko"    #Its a class variable/ static variable.Why we written class variable 'school' is, it effects all the objects.we dont need to access only for one object thats why we written class variable 'school'.
    def __init__(self,m1,m2,m3):  #we are passing parameters three values of m1,m2,m3
        self.m1=m1      #self is keyword that refers to object & m1 is instance variable. we assigned value m1
        self.m2=m2      #self is keyword that refers to object & m2 is instance variable. we assigned value m2
        self.m3=m3      #self is keyword that refers to object & m3 is instance variable. we assigned value m3
    def avg(self):         #This is an instance method that works with an object
        return(self.m1+self.m2+self.m3)/3
s1=student(34,47,32)  #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s2=student(89,32,12)  #Here s2 is object #It creates a new object of the student class and assigns it to the variable s2.Here new object is 's2'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
print(s1.avg())  #we are printing the s1 object with avg() method.
print(s2.avg())  #we are printing the s2 object with avg() method.

output:
37.666666666666664
44.333333333333336
______________________________________________________________________________________________________________
class student:                #class is keyword and student is class name
    school = "Telusko"        #Its a class variable/ static variable.Why we written class variable 'school' is, it effects all the objects.we dont need to access only for one object thats why we written class variable 'school'.
    def __init__(self,m1,m2,m3):  #we are passing parameters three values of m1,m2,m3
        self.m1=m1    #self is keyword that refers to object & m1 is instance variable. we assigned value m1
        self.m2=m2    #self is keyword that refers to object & m2 is instance variable. we assigned value m2
        self.m3=m3    #self is keyword that refers to object & m3 is instance variable. we assigned value m3
    def avg(self):            #This is an instance method that works with an object
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):  #it fetches the value, we say accessor
        return self.m1
    def set_m1(self,value): #it changes the value, we say mutator
        self.m1=value
s1=student(34,47,32) #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s2=student(89,32,12) #Here s2 is object #It creates a new object of the student class and assigns it to the variable s2.Here new object is 's2'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
print(s1.avg())   #we are printing the s1 object with avg() method.
print(s2.avg())   #we are printing the s2 object with avg() method.

output:
37.666666666666664
44.333333333333336
--------------------------------------------------------------------------------------------------------------
Class Method:
class student:                     #class is keyword and student is class name
    school = "Telusko"             #Its a class variable/ static variable.Why we written class variable 'school' is, it effects all the objects.we dont need to access only for one object thats why we written class variable 'school'.
    def __init__(self,m1,m2,m3):   #we are passing parameters three values of m1,m2,m3
        self.m1=m1          #self is keyword that refers to object & m1 is instance variable. we assigned value m1
        self.m2=m2          #self is keyword that refers to object & m2 is instance variable. we assigned value m2
        self.m3=m3          #sel3 is keyword that refers to object & m3 is instance variable. we assigned value m3
    def avg(self):          #This is an instance method that works with an object
        return (self.m1+self.m2+self.m3)/3
    @classmethod                  #Its a decorator, to create a class method. we are creating decorator
    def info(cls):                #info() method,passed 'cls' keyword as parameter will print name of the school
        return cls.school
s1=student(34,47,32)    #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s2=student(89,32,12)    #Here s2 is object #It creates a new object of the student class and assigns it to the variable s2.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
print(s1.avg())     #we are printing the s1 object with avg() method.
print(student.info()) #Here info() should work with all objects not with only one method.so,thats why we written class student

output:
37.666666666666664
Telusko
--------------------------------------------------------------------------------------------------------------
Static Method:
class student:                 #class is keyword and student is class name
    school = "Telusko"         #Its a class variable/ static variable.Why we written class variable 'school' is, it effects all the objects.we dont need to access only for one object thats why we written class variable 'school'.
    def __init__(self,m1,m2,m3):  #we are passing parameters three values of m1,m2,m3
        self.m1=m1       #self is keyword that refers to object & m1 is instance variable. we assigned value m1
        self.m2=m2       #self is keyword that refers to object & m2 is instance variable. we assigned value m2
        self.m3=m3       #self is keyword that refers to object & m3 is instance variable. we assigned value m3
    def avg(self):             #This is an instance method that works with an object
        return (self.m1+self.m2+self.m3)/3
    @classmethod               #Its a decorator, to create a class method. we are creating decorator
    def getschool(cls):      #Here we are not concerned about instance variable and not concerned about class variable. so, thats why written getschool() method using get keyword.#if we are using class variable, we suppose to use 'cls' keyword
        return cls.school
    @staticmethod              #Its a decorator
    def info():      #we are not relating this info() method to class and object.so, thats why we didnt pass any parameters
        print("This is student class...in abc module")
s1=student(34,47,32)   #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s2=student(89,32,12)   #Here s2 is object #It creates a new object of the student class and assigns it to the variable s2.Here new object is 's2'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
print(s1.avg())        #we are printing the s1 object with avg() method
print(student.getschool())  #Hence, we are not concerning about class and object because it is static method, as we defined classmethod using decorator. Here we use getschool() method to print the name of the school without using any object and class with parameters
student.info()  #we are calling the info() method using class name 'student' to execute

output:
37.666666666666664
Telusko
This is student class...in abc module
---------------------------------------------------------------------------------------------------------------
-In variables.There are two variables
(i)class variable/static variable
(ii)object/instance variable

-But, In the methods.There are three methods
(i)Instance Methods
(ii)Class Methods
(iii)Static Methods

-In instance method it has two methods
(i)Accessor Methods
(ii)Mutator Methods

Accessor Methods:
If we want to fetch the values of instance variable, we use accessor methods.

Mutator Methods:
If we want to modify the values, we use mutator methods.

get() method: it fetches the value, we say accessor
set() method: it changes the value, we say mutator

-if we are using class variable, we suppose to use 'cls' keyword
-if we are using instance variable, we suppose to use 'self' keyword