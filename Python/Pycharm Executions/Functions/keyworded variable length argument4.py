def person(name,**data):     #** indicates the argument can store multiple values with keywords
    print(name)
    print(data)
person(name='suman',age=24,city='vizag',mobileno=9392263295)

output:
suman
{'age': 24, 'city': 'vizag', 'mobileno': 9392263295}
---------------------------------------------------------------------------------------------------------------------
def person(name, **data):   #** indicates the argument can store multiple values with keywords
    print(name)
    for i,j in data.items():
       print(i,j)           #i is key and j is value
person('suman',age=24,city='vizag',mobileno=9392263295)

output:
suman
age 24
city vizag
mobileno 9392263295
----------------------------------------------------------------------------------------------------------------------
Variable length argument :
-- A variable-length argument is a feature that allows a function to accept an arbitrary number of arguments. 
The syntax for defining a variable-length argument in Python is to use an asterisk (*) before the parameter name.
e.g
def person(name,*data):
    print(name)
    print(data)
person('navin',28,9765432)

keyword variable length argument:
-- keyword variable length argument is a feature that allows a function to accept an arbitrary number of 
   keyword arguments.
-- use a double asterisk (**) to define a variable-length argument that accepts keyword arguments. 
For example:
The **kwargs parameter allows the function to accept an arbitrary number of keyword arguments. 
The function can then loop over the dictionary of keyword arguments and do something with them.
e.g
def person(name,**data):  #**kwargs
    print(name)
     for i, j in data:
        print(i,j)  #i is key and j is value
person('navin',aget=28,city='Mumbai',mob=9865432)
