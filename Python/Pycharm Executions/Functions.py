def greet():                 #def is defining function & greet() is function name.
    print("Hello")
    print("Good Morning")
greet()                      #we are calling the function then only it executes 

output:
Hello
Good Morning
----------------------------------------------------------------------------------------------------------------------
def greet():                  #def is defining function & greet() is function name.
    print("Good Evening")
    print("Hello,How are u")
greet()                      #we are calling the function for two times. so it executes for 2 times.
greet()

output:
Good Evening
Hello,How are u
Good Evening
Hello,How are u
----------------------------------------------------------------------------------------------------------------------
def add(x,y):             #add() is function name.In add() we passed x,y are arguments/parameters 
    c=x+y
    print(c)
add(5,3)                  #we are calling the function to execute

output:
8
--------------------------------------------------------------------------------------------------------------------
def add(x,y):
    c=x+y
    return c
result = add(5,5)       #we assigned/stored function add(5,5) to the 'result' variable.
print(result)

output:
10
----------------------------------------------------------------------------------------------------------------------
def add_sub(x,y):      #add_sub() is the function and x,y are arguments/parameters.
    c=x+y              #1st output
    d=x-y              #2nd output
    return c,d
result1,result2 = add_sub(5,2) #Here it is 2 rseults/outputs . so we have assigned 2 variables
print(result1,result2)

output:
7 3
---------------------------------------------------------------------------------------------------------------------
-- A function is a block of code that performs a specific task. 
-- Functions are used to break down larger programs into smaller and more manageable chunks, 
   making it easier to read, test, and debug code.
-- Functions can take input arguments, perform operations on them, and return output values.
-- To define a function in Python, you use the def keyword followed by the function name, 
   input parameters (if any), and a colon. The function body is then indented and contains the code to be executed.
   
Here's an example of a simple Python function that takes two arguments and returns their sum:
------------------------------------------------------------------------------------------------------------------
def add_numbers(a, b):
    sum = a + b
    return sum
add_numbers(4,5) # calling the function
-------------------------------------------------------------------------------------------------------------------
without calling the function cannot run

Arguments in python
-- whatever variable is used inside a function during the defining of the function is called a formal argument.
-- whatever value you passed during the calling is called actual arguments.

-- The return statement is used to exit a function and return a value. 
-- The return statement can be used to return a value from a function. 
-- The return statement can also be used to exit a function without returning a value.
-- If the return statement is without any expression, then the special value None is returned.
-- Functions without a return statement return None as their result.
def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(4,5)
print(result1,result2)  

The above code defines a Python function called add_sub that takes two input arguments x and y. 
The function first adds x and y and stores the result in a variable called c. 
It then subtracts y from x and stores the result in a variable called d. Finally, it returns both c and d as a tuple.


The function can be called with two arguments, as shown in the line result1,result2 = add_sub(4,5). 
This line assigns the values returned by the add_sub function to the variables result1 and result2, respectively. 
The print statement then outputs the values of result1 and result2 to the console.
