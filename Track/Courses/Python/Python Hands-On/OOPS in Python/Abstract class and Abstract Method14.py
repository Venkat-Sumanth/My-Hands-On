class computer:
    def process(self):
        pass  #Here we are declaring this method by writing pass to move forward but not defined or definition , we call them as abstract method.
com=computer() #com is object and computer() is constructor class,we created com object for the computer class
com.process()  #we are calling the process() method using com object

output:
NIL
---------------------------------------------------------------------------------------------------------------
from abc import ABC,abstractmethod  #To make it abstract class we supposed to import ABC , abstractmethod
class computer(ABC): #we make this class as sub class of ABC, then it became abstract class
    @abstractmethod   #we are telling to the compiler that this is abstractmethod using decorator
    def process(self):
        pass #Here we are declaring this method by writing pass to move forward but not defined or definition , we call them as abstract method.
class laptop(computer): #laptop is subclass of computer. #laptop class is inheriting computer class in which we have abstract method, so it compulsion to define process(self) method which is there in computer class
    def process(self):
        print('Running')
com1=laptop()  #com1 is object and laptop() is constructor class,we created com1 object for the laptop class
com1.process() #we are calling the process() method using com1 object

output:
Running
#A class which will have abstract method is called abstract classes.
#Abstract class will have one abstract method
--------------------------------------------------------------------------------------------------------------
from abc import ABC,abstractmethod  #To make it abstract class we supposed to import ABC , abstractmethod
class computer(ABC):  #we make this class as sub class of ABC, then it became abstract class
    @abstractmethod  #we are telling to the compiler that this is abstractmethod using decorator
    def process(self):
        pass  #Here we are declaring this method by writing pass to move forward but not defined or definition , we call them as abstract method.
class laptop(computer): #laptop is subclass of computer. #laptop class is inheriting computer class in which we have abstract method, so it compulsion to define process(self) method which is there in computer class
    def process(self):
        print('Running')
class whiteboard:
    def write(self):
        print('Its writing')
class programmer:
    def work(self,com):
        print('Solving Bugs')
        com.process() #to ensure it uses the process method of the passed object, which adheres to the Computer interface.
com1=laptop()  #com1 is object and laptop() is constructor class,we created com object for the laptop class
com2=whiteboard() #com2 is object and whiteboard() is constructor class,we created com object for the whiteboard class
prog1=programmer() #prog1 is object and programmer() is constructor class,we created com object for the programmer class
prog1.work(com1) #we are calling work() method using object prog1 by passing com1 object as parameter

output:
Solving Bugs
Running
#A class which will have abstract method is called abstract classes.
#Abstract class will have one abstract method
---------------------------------------------------------------------------------------------------------------