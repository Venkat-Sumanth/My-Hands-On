class Pycharm:  #class is keyword and Pycharm is class name
    def execute(self):   #we are defining execute() method
        print('compiling')
        print('Running')
class Laptop:    #class is keyword and Laptop is class name
    def code(self,ide): #we are defining code() method and passing ide variable as an argument/parameter in it.
        ide.execute #ide is object and execute is method , we are calling execute() method using object ide
ide=Pycharm() #ide is object and Pycharm() is constructor class that will call __init__ method.
lap1=Laptop() #lap1 is object and Laptop() is constructor class that will call __init__ method.
lap1.code(ide) #we are calling code() method using lap1 object by passing ide parameter

output:
compiling
Running
--------------------------------------------------------------------------------------------------------------
class Pycharm:      #class is keyword and Pycharm is class name
    def execute(self):
        print('Compiling')
        print('Running')
class MyEditor:   #class is keyword and Pycharm is class name
    def execute(self):
        print('Spell check')
        print('Convention Check')
        print('Compiling')
        print('Running')
class Laptop:     #class is keyword and Pycharm is class name
    def code(self,ide):  #we are defining code() method and passing ide variable as an argument/parameter in it.
        ide.execute()  #ide is object and execute is method , we are calling execute() method using object ide
ide=MyEditor()  #ide is object and MyEditor() is constructor class that will call __init__ method.
lap1=Laptop()   #lap1 is object and Laptop() is constructor class that will call __init__ method.
lap1.code(ide)  #we are calling code() method using lap1 object by passing ide parameter

output:
Spell check
Convention Check
Compiling
Running
----------------------------------------------------------------------------------------------------------------
Duck typing in Python is a concept where an object's suitability is determined by the presence of 
certain methods and properties, rather than the object's actual type. 
If an object has the necessary methods and properties, it can be used as the desired type.

If an object acts like a duck , then this is a duck.
If the object has the method  execute , that is an IDE 

#where the type or the class of an object is less important than the method it defines.
#don't care about it's type/class,  care about what it can do

Youtube Link:
https://www.youtube.com/watch?v=CuK0g8OFzwo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=63