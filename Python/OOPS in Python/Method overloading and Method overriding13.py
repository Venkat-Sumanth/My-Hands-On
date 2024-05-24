class student:
    def __init__(self,m1,m2): #we are passing parameters two values of m1,m2
        self.m1=m1  #self is keyword that refers to object & m1 is instance variable. we assigned value m1
        self.m2=m2  #self is keyword that refers to object & m2 is instance variable. we assigned value m2
    def sum(self,a,b,c):  #we defining sum() method and passing a,b,c as parameters
        s=a+b+c
        return s
s1=student(58,69) #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
print(s1.sum(5,9,1))

output:
15
---------------------------------------------------------------------------------------------------------------
Method Overloading:
Method overloading, it will have same method name but different parameters

class student:
    def __init__(self,m1,m2): #we are passing parameters two values of m1,m2
        self.m1=m1  #self is keyword that refers to object & m1 is instance variable. we assigned value m1
        self.m2=m2  #self is keyword that refers to object & m2 is instance variable. we assigned value m2
    def sum(self,a=None,b=None,c=None):  #we defining sum() method and passing a,b,c as parameters
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=student(58,69) #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
print(s1.sum(4,6))

output:
10
---------------------------------------------------------------------------------------------------------------
Method Overriding:
Method Overriding, it has same method name and same parameters

class A:
    def show(self):  #show() is function 
        print('in A show')
class B(A):  #Here B(A) means B is inherating(taking) all the features of A
    pass
a1=B()     #B() is constructor
a1.show()  #it should print all the details of a1 object

output:
in A show
#Here it first check B method, it doesnt have any statements . 
so, then it checks A then it prints A show() function print statements
_____________________________________________________________
class A:
    def show(self):
        print('in A show')
class B:
    def show(self):
        print('in B show')
a1=B()  #B() is constructor 
a1.show() #it should print all the details of a1 object

output:
in B show
#Here B show() has statements . so it prints B show() function statments.
---------------------------------------------------------------------------------------------------------------