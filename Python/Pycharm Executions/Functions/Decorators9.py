def div(a,b):
    print(a/b)
div(4,2)

output:
2.0
--------------------------------------------------------------------------------------------------------------
def div(a,b):
    print(a/b)
div(2,4)         #Here we need to swap 2,4 to 4,2 where here numerator is smaller than denominator

output:
0.5
--------------------------------------------------------------------------------------------------------------
def div(a,b):
    print(a/b)
def smart_div(func):  #Here we are passing the 'func' parameter.#Here simple way we can write 'if' condition, we can do swap. why we are writing function inside function is because the code will be avilable in other file, we need to import or we dont have access for this function or we dont want to change the code in existing function.
    def inner(a,b):   #we are writing function inside function and passing a,b parameters.
         if a<b:      #condition to swap in a function
            a,b=b,a   #we are swaping a=2,b=4 to a=4,b=2
         return func(a,b) #we are returning the values after swaping a=4,b=2
    return inner  #we are returning the inner function
div = smart_div(div) #we are connecting the inner function(smart_div) and outer function(div) to execute .#we are passing outer function as a parameter  
div(2,4) # we are calling the function by passing parametervalues 2,4 that will swap to a=4,b=2.

output:
2.0
--------------------------------------------------------------------------------------------------------------
- Functions are built to perform certain tasks.

Properties of functions:-
- We can also write a code for the function inside another function.
- We can assign a function to another function in python as a function is also an object.
- A function is an instance of the Object type.
- We can store the function in a variable.
- We can also pass the function as a parameter to another function.
- A function from a function can also be returned.

- Decorators are used to add extra features to the existing functions.
- Decorators can change the behaviour of an existing function at the compile itself.

Properties of Decorators:-
-The outer function is called the decorator, which takes the original function as an 
 argument and returns a modified version of it.
- Decorator contains an outer function that also takes a function as an argument.
- Inside the outer function, there is another function that takes a number of parameters 
  as per the logic as an argument.
- Inner function contains the code for the logic that must be contained in the previously 
  defined normal function.
- Inner function returns the values as per the required code that can be equal to the number 
  of arguments passes in an inner function.
- Outer function return an inner function.
- In the main code, we have to call the outer function of a decorator and pass the 
  normal function as an argument.