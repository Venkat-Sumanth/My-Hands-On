
>>> num = 5
>>> id(num)  #id is function used to get the address of an object #Here object is 5 
140718272924216
>>> name = 'suman'
>>> id(name)
1813439776448
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
140718272924376
>>> id(b)
140718272924376
>>> id(10)
140718272924376
>>> k = 10
>>> id(k)
140718272924376
>>> a = 9
>>> id(a)
140718272924344
>>> id(b)
140718272924376
>>> k = a
>>> id(a)
140718272924344
>>> id(k)
140718272924344
>>> b = 8
>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15
>>> type(PI)
<class 'float'>
-----------------------------------------------------------------------------------------------------------
- Every variable has its address.
- In Python, the id() function is used to get the address of a variable.
- We can also assign the value of one variable to any other variable.
- In python, whenever we create multiple variables and if they have the same data 
  then they will point towards the same box or same memory area.
- Everything is an object in Python.
- Variables are also known as tags as we tag the value with a variable.
- If the same variable store multiple values, then that variable will point towards the 
  new memory area where the new value is get stored.
  
- If there is any data present in the memory that is not referenced by any variable, 
  then that will be removed from the memory by the Garbage collector.

- The value of variables can be changed but the value of the constant remains the same.
- In python, we represent constants through capital letters.
- type() function is used to get the data type of value of a variable.
- Besides in-built data types, we can also create our own types.
