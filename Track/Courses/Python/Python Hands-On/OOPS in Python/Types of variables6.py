class car:    #class is keyword and car is class name
    def __init__(self):  #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'c1' and 'c2' are the two objects . so thats why it executes 2 times.            
        self.milage = 10 #self is object and 'milage' is attribute/instance variable.
        self.company = "BMW"  #self is object and 'company' is attribute/instance variable.
c1=car()  #Here c1 is object #It creates a new object of the car class and assigns it to the variable c1.Here new object is 'c1'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
c2=car()  #Here c1 is object #It creates a new object of the car class and assigns it to the variable c2.Here new object is 'c2'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
print(c1.company,c1.milage)  #c1,c2 are objects & company,milage are instance variables/attributes.
print(c2.company,c2.milage)  #c1,c2 are objects & company,milage are instance variables/attributes.

output:
BMW 10
BMW 10
---------------------------------------------------------------------------------------------------------------
class car:                #class is keyword and car is class name
    def __init__(self):   #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'c1' and 'c2' are the two objects . so thats why it executes 2 times.       
        self.milage = 10  #self is object and 'milage' is attribute/instance variable.
        self.company = "BMW" #self is object and 'company' is attribute/instance variable.
c1=car()  #Here c1 is object #It creates a new object of the car class and assigns it to the variable c1.Here new object is 'c1'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
c2=car()  #Here c2 is object #It creates a new object of the car class and assigns it to the variable c2.Here new object is 'c2'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
c1.milage = 8    #we are changing instance variable of 'milage' 10 to 8
print(c1.company,c1.milage)  #c1,c2 are objects & company,milage are instance variables/attributes.
print(c2.company,c2.milage)  #c1,c2 are objects & company,milage are instance variables/attributes.

output:
BMW 8
BMW 10
--------------------------------------------------------------------------------------------------------------
class car:              #class is keyword and car is class name
    wheels = 4          #class variable/static variable.
    def __init__(self): #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'c1' and 'c2' are the two objects . so thats why it executes 2 times.       
        self.milage = 20 #self is object and 'milage' is attribute/instance variable.
        self.company = "Audi"  #self is object and 'company' is attribute/instance variable.
c1=car()   #Here c1 is object #It creates a new object of the car class and assigns it to the variable c1.Here new object is 'c1'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
c2=car()   #Here c2 is object #It creates a new object of the car class and assigns it to the variable c2.Here new object is 'c2'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
c1.milage = 8  #we are changing instance variable of 'milage' 20 to 8
print(c1.company,c1.milage,c1.wheels)
print(c2.company,c2.milage,c2.wheels)

output:
Audi 8 4
Audi 20 4
--------------------------------------------------------------------------------------------------------------
class car:               #class is keyword and car is class name
    wheels = 4           #Its a class variable/ static variable.Why we written class variable 'wheels' is, it effects all the objects.we dont need to access only for one object thats why we written class 'wheels'.
    def __init__(self):  #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'c1' and 'c2' are the two objects . so thats why it executes 2 times.       
        self.company = "BENZ" #self is object and 'company' is attribute/instance variable.
        self.milage = 32      #self is object and 'milage' is attribute/instance variable.
c1=car()   #Here c1 is object #It creates a new object of the car class and assigns it to the variable c1.Here new object is 'c1'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
c2=car()   #Here c2 is object #It creates a new object of the car class and assigns it to the variable c2.Here new object is 'c2'.#Here 'car()' is that it instantiate and call __init__.#'car()' is a constructor and there we can pass the values.
c2.milage = 40 #we are changing instance variable of 'milage' 32 to 40
car.wheels = 5 #Its a namespace to modify the existing class variable and instance variable.
print(c1.company,c1.milage,c1.wheels) 
print(c2.company,c2.milage,c2.wheels)

output:
BENZ 32 5
BENZ 40 5
---------------------------------------------------------------------------------------------------------------
Important Note:
-Below the class the variables we write, we call it as class variables/ static variables
Ex:
class car:              
    wheels = 4          #class variable/static variable.
    def __init__(self):        
        self.milage = 20 
        self.company = "Audi"
#Here in the above code only 'wheels = 4' is class variable/static variable

-Below the __init__() method the variables we write, we call it as Attributes/instance variables.
Ex:
class car:              
    wheels = 4          
    def __init__(self):        
        self.milage = 20  #instance variable/attribute.
        self.company = "Audi"  #instance variable/attribute.
#Here in the above ccode we written below the __init__() method is instance variables/attributes.
The instance variables are milage and company.

-In memory namespace would be there.Namespace is an area where we create and store object/variable
-we have two double namespace 
(i)class namespace: Here we store all class variables
(ii)object/instance namespace: Here we create all the instance variables.

-In the below code
class car:              
    wheels = 4          #class namespace
    def __init__(self):        
        self.milage = 20  #instance namespace
        self.company = "Audi"  #instance namespace
