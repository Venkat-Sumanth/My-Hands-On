class A:
    def __init__(self):
        print('In A Init')
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('feature2 is working')
class B(A):                    #child class/sub class #Here class B is inheriting all the feature of A
    def feature3(self):
        print('Feature3 is working')
    def feature4(self):
        print('Feature4 is working')
a1=A()        #A() is constructor that will call __init__ method.

output:
In A Init
---------------------------------------------------------------------------------------------------------------
class A:
    def __init__(self):
        print('In A Init')
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('feature2 is working')
class B(A):         #child class/sub class #Here class B is inheriting all the feature of A
    def __init__(self):
        print('in B Init')
    def feature3(self):
        print('Feature3 is working')
    def feature4(self):
        print('Feature4 is working')
a1=B()   #B() is constructor that will call __init__ method.


output:
in B Init
--------------------------------------------------------------------------------------------------------------
class A:
    def __init__(self):
        print('in A init')
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('Feature2 is working')
class B(A):                  #child class/sub class #Here class B is inheriting all the feature of A
    def __init__(self):
        super().__init__()
        print('In B Init')
    def feature3(self):
        print('Feature3 is working')
    def feature4(self):
        print('Feature4 is working')
a1=B()        #B() is constructor that will call __init__ method.

output:
in A init
In B Init
--------------------------------------------------------------------------------------------------------------
class A:
    def __init__(self):
        print('in A init')
    def feature1(self):
        print('Feature1-a is working')
    def feature2(self):
        print('Feature2 is working')
class B:
    def __init__(self):
        print('In B Init')
    def feature1(self):
        print('Feature1-b is working')
    def feature4(self):
        print('Feature4 is working')
class C(A,B):                  #Here c have two super classes it means c inherites the features of super class A and super class B #In the concept of MRO it starts from left to right in the multiple inheritance. so it takes left one first. Here left one is only class A
    def __init__(self):
        super().__init__()  #we are calling the __init__ () method of class A # This method indicates that it inheritates the super class features to the child class/sub class. #In the concept of MRO it starts from left to right in the multiple inheritance
        print('In C Init')
a1=C()           #C() is constructor that will call __init__ method.
a1.feature1()    #Here it executes first one as it starts from left to right

output:
in A init
In C Init
Feature1-a is working
--------------------------------------------------------------------------------------------------------------
class A:
    def __init__(self):
        print('in A init')
    def feature1(self):
        print('Feature1-a is working')
    def feature2(self):
        print('Feature2 is working')
class B:
    def __init__(self):
        print('In B Init')
    def feature1(self):
        print('Feature1-b is working')
    def feature4(self):
        print('Feature4 is working')
class C(A,B):         #Here c have two super classes it means c inherites the features of super class A and super class B #In the concept of MRO it starts from left to right in the multiple inheritance. so it takes left one first. Here left one is only class A
    def __init__(self):
        super().__init__() #we are calling the __init__ () method of class A # This method indicates that it inheritates the super class features to the child class/sub class. #In the concept of MRO it starts from left to right in the multiple inheritance
        print('In C Init')
    def feat(self):
        super().feature2() #To represent the super class we use super() method.
a1=C()        #C() is constructor that will call __init__ method.
a1.feat()     #we are calling the feat() method

output:
in A init
In C Init
Feature2 is working
----------------------------------------------------------------------------------------------------------------
#when we create object of subclass it will call init of subclass first

#If we have call super then it will first call init of super class then call init of sub class

Method Resolution Order(MRO):
what happens here is it always starts from left to right.
The moment we say __init__(), it first goes to the object of its constructor class, 
then it executes the super classes first.


Youtube link:
https://www.youtube.com/watch?v=6P-P879BcHQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=61