class computer: #class is keyword and computer is class name.
    pass        #When the pass statement is executed, nothing happens, but we avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
c1=computer()   #Here c1 is object #It creates a new object of the computer class and assigns it to the variable c1.Here new object is 'c1'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
print(id(c1))   #we are printing the object c1 id using 'id' function

output:
1590736745968
---------------------------------------------------------------------------------------------------------------
class computer: #class is keyword and computer is class name.
    pass        #When the pass statement is executed, nothing happens, but we avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
c1=computer()   #Here c1 is object #It creates a new object of the computer class and assigns it to the variable c1.Here new object is 'c1'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
c2=computer()   #Here c2 is object #It creates a new object of the computer class and assigns it to the variable c1.Here new object is 'c2'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
print(id(c1))   #we are printing the object c1 id using 'id' function
print(id(c2))   #we are printing the object c2 id using 'id' function

output:
2383519710240
2383519709424
---------------------------------------------------------------------------------------------------------------
class computer:  #class is keyword and computer is class name.
    def __init__(self): #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'comp1' and 'comp2' are the two objects . so thats why it executes 2 times.            
        self.name='suman' #self is object and name is attribute
        self.age= 24      #self is object and age is attribute
c1=computer()         #Here c1 is object #It creates a new object of the computer class and assigns it to the variable c1.Here new object is 'c1'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
c2=computer()         #Here c2 is object #It creates a new object of the computer class and assigns it to the variable c1.Here new object is 'c2'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
print(c1.name)        #c1 is object and name is attribute
print(c2.name)        #c2 is object and age is attribute.

output:
suman
suman
---------------------------------------------------------------------------------------------------------------
class computer:             #class is keyword and computer is class name.
    def __init__(self):     #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'comp1' and 'comp2' are the two objects . so thats why it executes 2 times.            
        self.name = 'suman' #self is object and name is attribute
        self.age = 24       #self is object and age is attribute
c1=computer()     #Here c1 is object #It creates a new object of the computer class and assigns it to the variable c1.Here new object is 'c1'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
c2=computer()     #Here c2 is object #It creates a new object of the computer class and assigns it to the variable c2.Here new object is 'c2'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
c1.name='hemanth' #c1 is object and name is attribute
c2.age = 44       #c2 is object and age is attribute
print(c1.name,c1.age) #c1 is object and name,age are attributes.
print(c2.name,c2.age) #c2 is object and name,age are attributes.

output:
hemanth 24
suman 44
---------------------------------------------------------------------------------------------------------------
class computer:  #class is keyword and computer is class name.
    def __init__(self): #special method that is avilable in a class is '__init__'() #we are defining '__init__' method and passing the 'self' keyword as parameter.#Here '__init__' is used to initialize the variables #'__init__' method is calls automatically. It executes 2 times here because every object get calls once.#Here 'comp1' and 'comp2' are the two objects . so thats why it executes 2 times.            
        self.name = 'sumanth'   #self is object and name is attribute
        self.age = 24           #self is object and age is attribute
    def compare(self,other):  #Hence compare is not in-built function . so, we are defining compare method .
        if self.age == other.age:
              return True
        else:
              return False
c1=computer()     #Here c1 is object #It creates a new object of the computer class and assigns it to the variable c1.Here new object is 'c1'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
c1.age = 30       #c1 is object and age is attribute
c2=computer()     #Here c2 is object #It creates a new object of the computer class and assigns it to the variable c2.Here new object is 'c2'.#Here 'computer()' is that it instantiate and call __init__.#'computer()' is a constructor and there we can pass the values.
if c1.compare(c2): #As above we defined compare method because its not built-in function, Here c1 object is comparing with c2 object. #c1 object refers to 'self' in the defined compared method because c1 is calling.#c1 object is comparing itself with c2.#c1 is self and c2 is other            
    print("They are same")
else:
    print("They are different")
print(c1.name)  #c1 is object and name is attribute.
print(c2.name)  #c2 is object and name is attribute.

output:
They are different
sumanth
sumanth
--------------------------------------------------------------------------------------------------------------
-Every time we create an object it is allocated new space.

-size of an object is depends on the number of variables and size of each variable.

-constructor is responsible to assign or calculate the memory

-constructor will call '__init__' method . we need not call explicitly, it calls internally.
