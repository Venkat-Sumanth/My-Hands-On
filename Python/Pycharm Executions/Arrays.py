from array import *           #we write this line to import all the functions
values=array('i',[5,9,8,4,2])
print(values)

output:
array('i', [5, 9, 8, 4, 2])
--------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[2,6,8,5,-3,-4,-8])
print(values)

output:
array('i', [2, 6, 8, 5, -3, -4, -8])
-------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[5,6,7,8])
print(values.buffer_info())

output:
(2511536292416, 4) #Here buffer_info() function defines address and size of the values
--------------------------------------------------------------------------------------------------------------------
from array import *
values=array('i',[4,5,6,7])
print(values.typecode)

output:
i  # Here typecode function defines the datatype of values
-------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[7,8,9,10])
print(values.reverse())

output:
None  #Here reverse() function returns none because reverse() has to be written below the 'array of values'
----------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[2,5,6,8])
values.reverse()
print(values[0])

output:
8
-----------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[2,5,6,8])
values.reverse()
print(values[3])

output:
2
----------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[2,5,6,8])
for i in range(4):
     print(values[i])
     
output:
2
5
6
8
---------------------------------------------------------------------------------------------------------------------
from array import *
values=array('i',[1,2,3,-5])
values.reverse()
for i in range(4):
    print(values[i])

output:
-5
3
2
1
----------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[6,45,4,56])
values.reverse()
for i in range(len(values)):
    print(values[i])
    
output:
56
4
45
6
----------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[5,8,9,4,6])
values.reverse()
for e in values:
    print(e)
    
output:
6
4
9
8
5
--------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[2,5,6,8])
for j in values:
     print(j)

output:
2
5
6
8
---------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[5,7,45,65])
newArray = array(values.typecode,(m for m in values))
for e in newArray:
    print(e)

output:
5
7
45
65
-------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[25,14,63,85,3])
values.reverse()
newArray = array(values.typecode,(t*t for t in values))
for k in newArray:
    print(k)
    
output:
9
7225
3969
196
625
--------------------------------------------------------------------------------------------------------------------
from array import *
values = array('u',['y','t','h','d'])
for i in range(4):
    print(values[i])
    
output:
y
t
h
d
-----------------------------------------------------------------------------------------------------------------
from array import *
values = array ('u',['l','k','j','g'])
for y in values:
    print(y)
    
output:
l
k
j
g
---------------------------------------------------------------------------------------------------------------------
from array import *
values = array('i',[54,3,9,8])
newArray = array(values.typecode,(d*d for d in values))
i=0
while i<len(newArray):
    print(newArray[i])
    i=i+1
    
output:
2916
9
81
64