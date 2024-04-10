Using Temp variable:
>>>a=5
>>>b=6

>>>temp=a
>>>a=b
>>>b=temp
>>> print(a)
6
>>> print(b)
5
-----------------------------------------------------------------------------------------------------------
Without using any variable/third variable:
>>> a=5
>>> b=10
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print(a)
10
>>> print(b)
5

>>> a=5
>>> b=6
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print(a)
6
>>> print(b)
5

>>> a=2
>>> b=3
>>> a,b=b,a
>>> print(a)
3
>>> print(b)
2
