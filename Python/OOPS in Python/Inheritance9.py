class A:         #Parent class/super class
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('Feature2 is working')
a1=A()  #Here a1 is object and A() is constructor
a1.feature1()  #we are calling the feature1 method
a1.feature2()  #we are calling the feature2 method

output:
Feature1 is working
Feature2 is working
--------------------------------------------------------------------------------------------------------------
Single Level Inheritance:
class A:           #Parent class/super class
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('Feature2 is working')
class B(A):   #child class/sub class #Here class B is inheriting all the feature of A
    def feature3(self):
        print('Feature3 is working')
    def feature4(self):
        print('Feature4 is working')
a1=A()   #Here a1 is object and A() is constructor
a1.feature1() #we are calling the feature1 method
a1.feature2() #we are calling the feature2 method
b1=B()       #Here b1 is object and B() is constructor
b1.feature3()
b1.feature4()

output:
Feature1 is working
Feature2 is working
Feature3 is working
Feature4 is working
---------------------------------------------------------------------------------------------------------------
Multi Level Inheritance:
class A:               #Parent class/super class
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('Feature2 is working')
class B(A):     #child class/sub class #Here class B is inheriting all the feature of A
    def feature3(self):
        print('Feature3 is working')
    def feature4(self):
        print('Feature4 is working')
class C(B):   #child class/sub class #Here class c is inheriting all the feature of B
    def feature5(self):
        print('Feature5 is working')
a1=A()    #Here a1 is object and A() is constructor
a1.feature1()  #we are calling the feature1 method
a1.feature2()  #we are calling the feature2 method
b1=B()        #Here b1 is object and B() is constructor
b1.feature3()
b1.feature4()
c1=C()       #Here c1 is object and C() is constructor
c1.feature5()

output:
Feature1 is working
Feature2 is working
Feature3 is working
Feature4 is working
Feature5 is working
--------------------------------------------------------------------------------------------------------------
Multiple Inheritance:
class A:             #Parent class/super class
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('Feature2 is working')
class B:
    def feature3(self):
        print('Feature3 is working')
    def feature4(self):
        print('Feature4 is working')
class C(A,B):        #child class/sub class #Here class c is inheriting all the feature of A,B. 
    def feature5(self):
        print('Feature5 is working')
a1=A()   #Here a1 is object and A() is constructor
a1.feature1() #we are calling the feature1 method
a1.feature2() #we are calling the feature2 method
b1=B()       #Here b1 is object and B() is constructor
b1.feature3()
b1.feature4()
c1=C()        #Here c1 is object and C() is constructor
c1.feature5()

output:
Feature1 is working
Feature2 is working
Feature3 is working
Feature4 is working
Feature5 is working
---------------------------------------------------------------------------------------------------------------
Youtube class link:
https://www.youtube.com/watch?v=Cn7AkDb4pIU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=60