
>>>num = 2.5
>>>type(num)
<class 'float'>

>>>num = 5
>>>type(num)
<class 'int'>

>>>num = 6+9j
>>>type(num)
<class 'complex'>

>>>a = 5.6
>>>b = int(a)
>>>type(b)
<class 'int'>

>>>b
5

>>>k = float(b)
>>>k
5.0

>>>k = 6
>>>c = complex(b,k)
>>>c
(5+6j)

>>>b<k
True

>>>bool = b<k
>>>bool
True
>>>type(bool)
<class 'bool'>

>>>b>k
False

>>>int(true)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?

>>>int(True)
1
>>>int (False)
0

>>>lst = [25,36,45,12]
>>>type(lst)
<class 'list'>

>>>s = {25,36,45,15,12,25}
>>>s
{36, 25, 12, 45, 15}
>>>type(s)
<class 'set'>

>>> t = (25,36,4,57,12)
>>> type(t)
<class 'tuple'>

>>> str = "sumanth"
>>> type(str)
<class 'str'>

>>> st = 'a'
>>> type(st)
<class 'str'>

>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>

>>> d = {'navin':'samsung','rahul':'iphone','kiran':'oneplus'}
>>> d
{'navin': 'samsung', 'rahul': 'iphone', 'kiran': 'oneplus'}
>>> d.keys()
dict_keys(['navin', 'rahul', 'kiran'])
>>> d.values()
dict_values(['samsung', 'iphone', 'oneplus'])
>>> d['rahul']
'iphone'

>>> d('kiran')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d('kiran')
TypeError: 'dict' object is not callable

>>> d.get['kiran']
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d.get['kiran']
TypeError: 'builtin_function_or_method' object is not subscriptable

>>> d['kiran']
'oneplus'
>>> d.get('kiran')
'oneplus'
-----------------------------------------------------------------------------------------------------------
Python has several built-in data types. Here are some of the most common ones:
i) NoneType: This is a special data type that represents the absence of a value. It is similar 
   to null in other languages.
ii) Numbers: These can be integers, floating-point numbers, or complex numbers.
iii) Booleans: These are values that represent True or False.
iv) Lists: These are ordered collections of objects, enclosed in square brackets.
v) Tuples: These are similar to lists, but are immutable (i.e., their contents cannot be changed), 
   and are enclosed in parentheses.
vi) Sets: These are unordered collections of unique elements, enclosed in curly braces.
vii) Strings: These are sequences of characters, enclosed in single or double quotes.
viii) Ranges: These are immutable sequences of numbers, and are commonly used to iterate over 
      a sequence of numbers in a for loop.
ix) Dictionaries: These are collections of key-value pairs, enclosed in curly braces.
 
i)None Type
a=None
type(a)

ii)Numbers
int: if we want to assign a integer value to a variable 
a=5
type(a)

float: if we want to assign a float value to a variable 
num =2.5 
type(num) 

complex: if we we to assign a complex value to a variable
num =2+9j 
type(num)

Type conversion:  if we convert one data type to another data type 
>a=5.6
>b=int(a) 
>type(b) # output : int
>k=float(b) 
>type(k) # output : float
>c=complex(4,5)
>type(c) # output : complex

iii)boolean: if you want to assign a variable with a boolean value
>a= True
>type(a)  # output : bool
>bool=3 < 5 
True 
type(bool)

Sequence data types : if we want to assign a variable with multiple values 
List, Tuple, Set, String, Range

iv) List  if we want to assign a variable with multiple values and we want to change the values 
-- In Python, a list is a collection of ordered and mutable elements enclosed
in square brackets. Lists are one of the most commonly used data structures in 
Python because of their versatility and flexibility.
--lst=[25,36,45,12]
type(lst) # output : list

v) Tuple:  if we want to assign a variable with multiple values and we donot want 
   to change the values make immutable 
-- In Python, a tuple is a collection of ordered and immutable elements enclosed in parentheses. 
Tuples are similar to lists, but they cannot be modified once they are created, which makes them 
useful for storing data that should not be changed during the program's execution.
--t=(25,36,45,12,7)
type(t) # output : tuple

vi) Set:  if we want to assign a variable with multiple values and we donot want to change 
    the values and we donot want to duplicate values 
-- In Python, a set is an unordered collection of unique elements enclosed in curly braces.
Sets are useful for storing data that should not contain duplicates, such as a list of
users on a website.
--s={25,36,45,12,25,36}
type(s) # output : set
#output: {36, 12, 45, 25}

vii) String: if we want to assign sequence of characters to a variable
-- In Python, a string is a sequence of characters enclosed in single or double quotes.
Strings are immutable, which means that they cannot be modified once they are created.
str = "hello"
type(str) # output : str

--we are not talk about char data type in python
  st='a' # every character is a string in python

viii) Range: if we want to assign a variable with multiple values and we don't want to 
      change the values and we want to generate a sequence of numbers
-- In Python, a range is a sequence of numbers that is immutable and iterable.
Ranges are commonly used to iterate over a sequence of numbers in a for loop.
range(10) # range data type
type(range(10))  # output : range 
list(range(2,10,2)) # output : [2, 4, 6, 8]

ix) Dictionary:  if we want to assign a variable with multiple values and we donot want 
    to change the values and we want to assign a key to each value 
-- In Python, a dictionary is a collection of key-value pairs enclosed in curly braces.
Dictionaries are useful for storing data that is associated with a key, such as a list of
users on a website and their corresponding email addresses.
d={1:'a',2:'b',3:'c'}
type(d)
d1={'navin':'samsung','rahul':'iphone','kiran':'oneplus'} 
d1.values() # output : dict_values(['samsung', 'iphone', 'oneplus'])
d1.keys() # output : dict_keys(['navin', 'rahul', 'kiran'])
d['rahul'] #output : 'iphone'
d1.get('kiran') #output : 'oneplus'