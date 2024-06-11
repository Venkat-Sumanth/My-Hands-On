a=5
b=6
print(a+b)
print(int.__add__(a,b))

output:
11 #print(a+b)
11 #print(int.__add__(a,b))
------------------------------------------------------------------------------------------------------------
a='5'
b='6'
print(a+b)
print(str.__add__(a,b))

output: #it concatenated here
56
56
-------------------------------------------------------------------------------------------------------------
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):  # defined __add__() method because , int know whats +, string know whats +, but class student doesn't know whats +. so that's why we defined add method
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2) #s3 is object, student is constructor class, we passed m1,m2 as parameters
        return s3 
s1=student(58,69) #s1 is object and student is constructor class, we passed arguments in it
s2=student(60,65) #s2 is object and student is constructor class, we passed arguments in it
s3=s1+s2
print(s3.m1)

output:
118
--------------------------------------------------------------------------------------------------------------
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other): #we defined __add__() method because , int know whats +, string know whats +, but class student doesn't know whats +. so that's why we defined add method
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)  #s3 is object, student is constructor class, we passed m1,m2 as parameters
        return s3
    def __gt__(self,other): #greater than method
        s1=self.m1+self.m2  #s1 is variable of integer
        s2=other.m1+other.m2 #s1 is variable of integer
        if s1>s2:
            return True
        else:
            return False
    def __str__(self): 
        return self.m1,self.m2
s1=student(58,69) #s1 is object and student is constructor class, we passed arguments in it
s2=student(70,65) #s2 is object and student is constructor class, we passed arguments in it
s3=s1+s2
if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')
a=9
print(a.__str__()) # __str__() method is defined to return a formatted string representation of the object.
print(s1.__str__()) # __str__() method is defined to return a formatted string representation of the object.

output:
s2 wins
9
(58, 69)
---------------------------------------------------------------------------------------------------------------
Youtube link:
https://www.youtube.com/watch?v=9wd50TKv_OQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=64