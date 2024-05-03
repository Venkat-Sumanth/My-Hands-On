class computer:  #'class' is a keyword and 'computer' is class name.
    def config(self): #we are defining 'config' method and passing 'self' keyword as parameter .
        print("i5, 16gb, 1TB")
x=9
print(type(x)) #Here type() functions returns which datatype of variable is. 
a='8'
print(type(a))
comp = computer() #Here comp is object #It creates a new object of the computer class and assigns it to the variable comp.
print(type(comp))

output:
<class 'int'>
<class 'str'>
<class '__main__.computer'> #'__main__' is module name because we are running the code from here. if we import this to other file then that particular module name returns in the '__main__' place in this file. #computer is class name.
#After writing the class and class name .we have to put attributes and behaviour.
#Attributes are variables
#Behaviour is methods(functions).But here we call it as methods.
#Python type() is a built-in function that returns the type of an object. 
 It can be used to check the type of a variable, or to create a new type of object.
--------------------------------------------------------------------------------------------------------------
class computer: #'class' is a keyword and 'computer' is class name.
    def config(self): #we are defining 'config' method and passing 'self' keyword as parameter .
         print("i5, 16gb, 1TB")
comp1=computer() #Here comp1 is object #It creates a new object of the computer class and assigns it to the variable comp1.Here new object is 'comp1'
comp2=computer() #Here comp2 is object #It creates a new object of the computer class and assigns it to the variable comp2.Here new object is 'comp2'
computer.config(comp1) #if we want to use a method we suppose to use class name first, which that belongs to class name and method name. #Here class name is 'computer' and method name is 'config'. Then we are passing 'comp1' object as a parameter in it.
computer.config(comp2) #if we want to use a method we suppose to use class name first, which that belongs to class name and method name. #Here class name is 'computer' and method name is 'config'. Then we are passing 'comp2' object as a parameter in it.
comp1.config() #Here we are using object itself to call the method/function.#Here object is 'comp1' and 'config' is method/function.
comp2.config() #Here we are using object itself to call the method/function.#Here object is 'comp2' and 'config' is method/function.

output:
i5, 16gb, 1TB #This line executes from 'computer.config(comp1)'
i5, 16gb, 1TB #This line executes from 'computer.config(comp2)'
i5, 16gb, 1TB #This line executes from 'comp1.config()'
i5, 16gb, 1TB #This line executes from 'comp2.config()'
----------------------------------------------------------------------------------------------------------------
- Class is a blueprint to create objects.
- Integer, Float, String, etc., are in-built types in Python.
- To create our type like a computer, we have to create our own class for it. 
- To use the type that you have created, you need to define a class for it.
- A class can be defined by using the class keyword and every class must have a name to it.

The syntax for creating a class:-
class class_name:
methods():
statements
variables

- A class consists of two things:
1. Attributes  - Variables
2. Behaviour - Methods (Functions)

- An object of a class can be defined by a  variable and assigned its value with the type of the class.
- A class can have multiple objects.

Syntax of creating an object:-
 object variable = class_name()
 
- type() return the type of a value that is present inside the variable.
- If we will return the type of an object, then it will print the class name. It means an 
  object belongs to a type of particular class.
- String, integer, etc are also object that belongs to some in-build class like str and int respectively.

- We can call any method from a class.
- The behaviour of every object will be different from each other so need to define for which object, 
  you are calling a method.
- So, we need to pass an object in it as a parameter at the time of calling a method.

The syntax for calling a method:-
 class_name.method_name(object variable)

- We pass an object to a method as an argument that will go into the self.
- Self is the object that you are passing in a method.
- We can also call a method in another way:
 object_variable.method_name()

