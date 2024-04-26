In this lecture, we are discussing types of arguments in python :
-- formal argument
-- actual argument 

Actual arguments have 4 types:
1)position 
2)keyword
3)default
4)variable length argument  

---------------------------------------------------------------------------------------------------------------------
Position:
def person(name,age):
    print(name)
    print(age)
person('sumanth',24)   #Here ('sumanth',24) is the position to the defined function of (name,age)

output:
sumanth
24
----------------------------------------------------------------------------------------------------------------------
Keyword:
def person(name,age):
    print(name)
    print(age)
person(name='sumanth',age=24)  #Here name and age are the keywords.

output:
sumanth
24
---------------------------------------------------------------------------------------------------------------------
Default:
def person(name,age=24):
    print(name)
    print(age)
person('sumanth')        #if we doesnt define any value then it takes the default value in defined function.

output:
sumanth
24
----------------------------
def person(name,age=24):
    print(name)
    print(age)
person('sumanth',26)  #if we define the value in calling function then it takes only written value in calling function.

output:
sumanth
26
----------------------------------------------------------------------------------------------------------------------
Variable length Argument:
def sum(a,*b):         # *b indicates that it store multiple values 
    print(a)
    print(b)
sum(5,6,34,78)

output:
5
(6, 34, 78)
---------------------
def sum(*b):           # *b indicates that it store multiple values 
    c=0
    for i in b:
        c=c+i
    print(c)
sum(5,6,34,78)

output:
123
---------------------------------------------------------------------------------------------------------------------
Position argument:
-- During a function call, values passed through arguments should be in the order of parameters in the 
function definition. This is called positional arguments.
e.g:
def person(name,age):
    print(name)
    print(age)
add('sumanth',6)

keyword argument:
-- During a function call, values passed through arguments don’t need to be in the order of 
   parameters in the function definition. Keyword arguments can achieve this. 
-- All the keyword arguments should match the parameters in the function definition.
e.g 
person(age=28,name='navin') 

default argument: 
-- Default arguments are values that are provided while defining functions.
-- The assignment operator = is used to assign a default value to the argument.
-- Default arguments become optional during the function calls.
-- If we provide a value to the default arguments during function calls, it overrides the default value.
-- The function can have any number of default arguments.
-- Default arguments should follow non-default arguments.
e.g
def person(name,age=28):
    print(name)
    print(age)
person('navin')

variable length argument:
-- if you want to pass multiple value in a function call we can use variable length argument
def sum(*b):           # *b indicates that it store multiple values 
    c=0
    for i in b:
        c=c+i
    print(c)
sum(5,6,34,78)
