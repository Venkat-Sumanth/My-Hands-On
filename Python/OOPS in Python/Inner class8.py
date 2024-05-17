class student:        #class is keyword and student is class name
    def __init__(self,name,rollno):  #we are passing parameters two values of name,rollno
        self.name = name #self is keyword that refers to object & name is instance variable. we assigned value name
        self.rollno = rollno #self is keyword that refers to object & rollno is instance variable. we assigned value rollno
s1=student('Navin',2) #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s2=student('Jenny',3) #Here s2 is object #It creates a new object of the student class and assigns it to the variable s2.Here new object is 's2'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
print(s1.name,s1.rollno)

output:
Navin 2
-------------------------------------------------------------------------------------------------------------
class student:         #class is keyword and student is class name
    def __init__(self,name,rollno): #we are passing parameters two values of name,rollno
        self.name = name  #self is keyword that refers to object & name is instance variable. we assigned value name
        self.rollno = rollno #self is keyword that refers to object & rollno is instance variable. we assigned value rollno
    def show(self): #we define show() method to provide a way to display the contents of an object.
        print(self.name,self.rollno)
s1=student('Navin',2) #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s2=student('Jenny',3) #Here s2 is object #It creates a new object of the student class and assigns it to the variable s2.Here new object is 's2'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s1.show()  #it should print all the details of s1 object


output:
Navin 2
--------------------------------------------------------------------------------------------------------------
class student:        #outer class #class is keyword and student is class name     
    def __init__(self,name,rollno  #we are passing parameters two values of name,rollno
        self.name = name  #self is keyword that refers to object & name is instance variable. we assigned value name
        self.rollno = rollno #self is keyword that refers to object & rollno is instance variable. we assigned value rollno
        self.lap = self.laptop() #we have created the object for inner class-laptop class
    def show(self):  #we define show() method to provide a way to display the contents of an object.
        print(self.name,self.rollno)
        self.lap.show() #we are writing the class variable 'lap' to execute.
    class laptop:  #inner class #class is keyword and laptop is class name #we are writing the class inside the student class to get the group #we have to create the object in the outer class __init__() method.
        def __init__(self):
            self.brand = 'HP'  #brand is variable and HP is value
            self.cpu = 'i5'    #cpu is variable and i5 is value
            self.ram = 8       #ram is variable and 8 is value
        def show(self): #we define show() method to provide a way to display the contents of an object.
            print(self.brand,self.cpu,self.ram)
s1=student('Navin',2) #Here s1 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's1'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s2=student('Jenny',3) #Here s2 is object #It creates a new object of the student class and assigns it to the variable s1.Here new object is 's2'.#Here 'student()' is that, it instantiate and call __init__.#'student()' is a constructor and there we can pass the values.
s1.show     #it should print all the details of s1 object
lap1=s1.lap  #we are creating the lap1&lap2 are two objects for laptop class
lap2=s2.lap  #we are creating the lap1&lap2 are two objects for laptop class
print(id(lap1))
print(id(lap2))

output:
Navin 2
HP i5 8
2557688405536
2557688405824
---------------------------------------------------------------------------------------------------------------