
2+3
5

x=2
x+3
5

y=3
x+y
5

x=9
x+y
12

x
9

y
3

abc
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?

x+10
19

_+y -> /*_ indicates the previous outcome of operation*/
22

name = 'youtube'
        0123456 ->/*Index numbers*/
name
'youtube'

name + 'rocks'
'youtuberocks'

name 'rocks'
SyntaxError: invalid syntax

name [0]
'y'

name [5]
'b'

name [7]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name [7]
IndexError: string index out of range

name [-1]
'e'
name [-2]
'b'
name [-3]
'u'
name [-4]
't'
name [-5]
'u'
name [-6]
'o'
>>> name [-7]
'y'
>>> name [0:2]
'yo'
>>> name [1:5]
'outu'
>>> name [1:]
'outube'
>>> name [:7]
'youtube'
>>> name [:8]
'youtube'
>>> name [:6]
'youtub'
>>> name [3:10]
'tube'

>>>  'my' + name [3:]
...  
SyntaxError: unexpected indent

>>> 'my ' + name [3:]
'my tube'
>>> myname = 'Venkat Sumanth Bethanapalli'
>>> len(myname)
27
>>> myname [0:7]
'Venkat '
>>> myname [0:8]
'Venkat S'
>>> myname [0:15]
'Venkat Sumanth '

>>> myname [-13]4
SyntaxError: incomplete input

>>> myname [-13]
' '
>>> myname[-12]
'B'
>>> myname [-11]
'e'
>>> myname [-13:]
' Bethanapalli'
>>> myname [-14]
'h'
>>> myname [-9:]
'hanapalli'
>>> myname [-17:]
'anth Bethanapalli'
--------------------------------------------------------------------------------------------------------------------
-If I want to use output of previous operation so we use underscore (_) 

Use String as a variable:
Strings in python are surrounded by either single quotation marks, or double quotation marks.
e.g  "shiva" ,'shiva'

Assign String to a Variable:
Assigning a string to a variable is done with the variable name followed by an equal sign and the string
name='shiva'
name
shiva
   

Slicing String:
we can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon(:), to return a part of the string.
   