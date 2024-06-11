a=10                                 #Here a is Global varibale
def something():                     #we are defining the function named something()
    a=15                             #Here a is Local variable
    print("in function ",a)          #Printing the local variable a
something()                          #we are calling the function to execute.
print("outside ",a)                  #Printing the global variable a.

output:
in function  15
outside  10
#In functions firstly, local variable executes after that global variables executes.
----------------------------------------------------------------------------------------------------------------------
a=10                                #Here a is Global varibale
def something():
    print("inside function ", a)
something()
print("outside function ",a)

output:
inside function  10 #Here we didnt written local variable .so it prints the global varibal as local variable as output
outside function  10 
-----------------------------------------------------------------------------------------------------------------------
a=10                                 #Here a is Global varibale
def something():
    global a                         #Here global is a keyword.
    a=15                             #It considers a as global variable.
    print("inside function ",a)
something()
print("outside function ",a)

output:
inside function  15 
outside function  15                #As we defined global keyword it returns the global variable in inner function.
----------------------------------------------------------------------------------------------------------------------
a=10                                #Here a is Global varibale
print(id(a))                        #It prints the address of a
def something():
    a=9
    x=globals()['a']       #Here we used globals() function to access the global variable address a
    print(id(x))                    #It prints the address of a
    print("inside function ",a)
something()
print("outside function ",a)

output:
140719587969752
140719587969752
inside function  9
outside function  10
----------------------------------------------------------------------------------------------------------------------
a=10                              #Here a is Global varibale
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    print("inside function ",a)
    globals()['a']=15           #we are changing the value of global variable 'a' without effecting the local variable. 
something()
print("outside function ",a)

output:
140719587969752
140719587969752
inside function  9
outside function  15
----------------------------------------------------------------------------------------------------------------------
#1 Scope of variable
-- scope of variable means where we can access the variable
-- there are two types of scope of variable
    1. local scope
    2. global scope
    
#2 Local variable
-- local variable means variable which is defined inside the function
-- we can access the local variable inside the function only
-- we cannot access the local variable outside the function

Local Scope:
When a variable or function is defined inside a function, it is said to be in the local scope of that function. 
Variables defined in the local scope are only accessible within that function and are destroyed once the function 
completes execution. Local variables have the highest priority in accessing over global variables of the same name.
Ex:
def func():
    x = 10
    print(x)
func()
--  the variable x is defined inside the function, and it can only be accessed within the function.

#3 Global variable
-- global variable means variable which is defined outside the function
-- we can access the global variable inside the function
-- we can access the global variable outside the function
Ex:
x = 10
def func():
    print(x)
func()
-- the variable x is defined outside the function, and it can be accessed within the function.

#4 Global keyword
-- if we want to access the global variable inside the function and we want to change the value of 
global variable inside the function then we have to use global keyword.
Ex:
x = 10
def func():
    global x
    x = 15
    print(x)
func()
-- in this case no new variable is created inside the function, 
but the global variable x is accessed and modified inside the function.

#5 Global() function
-- if we want to access the global variable inside the function and we want to change the value of  global variable 
inside the function then we have to use global() function. 
Ex:
x = 10
def func():
    x = 15
    print("local x: ",x)
    y = globals()['x']
    print("global x: ",y)
    globals()['x'] = 20
-- using globals()['x'] we can access the global variable x inside the 
function and we can change the value of global variable x inside the function.


