class computer:  #'class' is a keyword and 'computer' is class name.
    def __init__(self): #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'comp1' and 'comp2' are the two objects . so thats why it executes 2 times.                                            
        print("in init")
    def config(self):  #we are defining 'config' method and passing 'self' keyword as parameter .
        print("i5, 16gb, 1TB")
comp1 = computer() #Here comp1 is object #It creates a new object of the computer class and assigns it to the variable comp1.Here new object is 'comp1' #Here 'computer()' is that it instantiate and call __init__ .#'computer()' is a constructor and there we can pass the values.       
comp2 = computer() #Here comp2 is object #It creates a new object of the computer class and assigns it to the variable comp2.Here new object is 'comp2' #Here 'computer()' is that it instantiate and call __init__ .#'computer()' is a constructor and there we can pass the values. 
comp1.config()  #Here we are using object itself to call the method/function.#Here object is 'comp1' and 'config' is method/function.
comp2.config()  #Here we are using object itself to call the method/function.#Here object is 'comp2' and 'config' is method/function.

output:
in init
in init
i5, 16gb, 1TB
i5, 16gb, 1TB
#special has one variable and one method
(i)special variable:
    __name__
(ii)special Method:   #Here we are using only special method to intialize the variables.
     __init__ 

Constructor:
constructor in Python is a special class method for creating and initializing an object instance at that class.
In Python every class has a constructor; it's not required to define explicitly. 
The purpose of the constructor is to construct an object and assign a value to the object's members.
Ex:-comp1 = computer()
    comp2 = computer()
#__init__ method in Python is used to initialize objects of a class. It is also called a constructor.

Self Keyword:
-The self keyword is used in Python classes to refer to the instance of the class. 
 It is used as the first parameter of all class methods.
-When we call a method on a class instance, Python automatically passes the instance as the first argument 
 to the method. This is why the self parameter is always the first parameter in a class method.
-The self keyword allows you to access the attributes and methods of the class from within the method
---------------------------------------------------------------------------------------------------------------
class computer:    #'class' is a keyword and 'computer' is class name.
    def __init__(self,cpu,ram): #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' parameter.#Here '__init__' is used to initialize the variables #'__init__' method  calls automatically. It executes 2 times here because every object get calls once.#Here 'comp1' and 'comp2' are the two objects . so thats why it executes 2 times. #Here we are passing the computer class parameters 'CPU' and 'RAM' to initialize to execute          
        self.cpu=cpu #cpu&ram are part of the object in the __init__ method. Here 'self' is an object
        self.ram=ram #cpu&ram are part of the object in the __init__ method. Here 'self' is an object
    def config(self):  #we are defining 'config' method and passing 'self' keyword as parameter.
        print("config is",self.cpu,self.ram) #Here cpu&ram are not local variable, those are objects. so thats why we are passing object 'self'. #we are passing 'self' which is object here to fetch the values. 
comp1 = computer('i5',16) #Here comp1 is object #It creates a new object of the computer class and assigns it to the variable comp1.Here new object is 'comp1' #Here 'computer()' is that it instantiate and call __init__ .#'computer()' is a constructor and there we can pass the values. #we are passing the two parameters here is cpu 'i5' and RAM 16 #Now we have to pass the 'cpu' and 'RAM' as parameters in '__init__' method to initialize #Here generally we are passing two parameters cpu&ram but in the backend it takes three parameters. 1st is object name 'comp1', 2nd is 'cpu', 3rd is 'RAM' 
comp2 = computer('ryzen',8) #Here comp2 is object #It creates a new object of the computer class and assigns it to the variable comp2.Here new object is 'comp2' #Here 'computer()' is that it instantiate and call __init__ .#'computer()' is a constructor and there we can pass the values. #we are passing the two parameters here is cpu 'Ryzen 3' and RAM 8 #Now we have to pass the 'cpu' and 'RAM' as parameters in '__init__' method to initialize #Here generally we are passing two parameters cpu&ram but in the backend it takes three parameters. 1st is object name 'comp2', 2nd is 'cpu', 3rd is 'RAM' 
comp1.config()  #Here we are using object itself to call the method/function.#Here object is 'comp1' and 'config' is method/function.
comp2.config()  #Here we are using object itself to call the method/function.#Here object is 'comp2' and 'config' is method/function.

output:
config is i5 16
config is ryzen 8
---------------------------------------------------------------------------------------------------------------
- Every object has two things: Attributes and Behaviour.
- Attributes are variables and behaviour is methods that are similar to functions.
- In python, variables will be defined in a special method known as _init_ that should be present inside the 
  class.
  
- init() method must have an argument known as self with it.
 def __init__(self):
 
- init() method in python works similarly to constructors that are present in other programming languages.
- init() runs automatically as we do not need to call this method.
- All methods other than init() will be executed only when they are called from somewhere in a program.
- For every object, init() method will be get called once. So, if we create two objects then the init() 
  method will execute two times.
  
- When an object of a class is created, the class is said to be instantiated. 
  It is also known as object creation.
  variable= class_name()
  
An object of that class will be created.
- We can pass arguments to a class in the constructor itself for their execution.
- Values of arguments can be accepted in a class in the init() method as its parameters.

- The variable name of the object is passed automatically and gets accepted by the self in the init() method.
 class Computer: 
  def __init__(self, CPU, ram):
 com1=Computer('i5', '16')
 
- So, in actuality when the object is created, first we pass the object itself in an argument and 
 then pass values of other parameters in it.
 
- Whatever values you passed for different parameters in an object, will be assigned to an object 
 through the self.
 def __init__(self, CPU, ram):
 
- In a class variables are not local variables as they are associated with an object 
 so we have to use the self with variables to fetch the values.
- We bind data with every object so one object will have its own methods and variables.
 