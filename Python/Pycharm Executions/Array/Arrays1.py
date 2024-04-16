from array import *
values=array('i',[5,9,8,4,2])
print(values)

from array import *
values = array('i',[2,6,8,5,-3,-4,-8])
print(values)

from array import *
values = array('i',[5,6,7,8])
print(values.buffer_info())

from array import *
values=array('i',[4,5,6,7])
print(values.typecode)

from array import *
values = array('i',[7,8,9,10])
print(values.reverse())

from array import *
values = array('i',[2,5,6,8])
values.reverse()
print(values[0])

from array import *
values = array('i',[2,5,6,8])
values.reverse()
print(values[3])

from array import *
values = array('i',[2,5,6,8])
for i in range(4):
     print(values[i])

from array import *
values=array('i',[1,2,3,-5])
values.reverse()
for i in range(4):
    print(values[i])

from array import *
values = array('i',[6,45,4,56])
values.reverse()
for i in range(len(values)):
    print(values[i])

from array import *
values = array('i',[5,8,9,4,6])
values.reverse()
for e in values:
    print(e)

from array import *
values = array('i',[2,5,6,8])
for j in values:
     print(j)

from array import *
values = array('i',[5,7,45,65])
newArray = array(values.typecode,(m for m in values))
for e in newArray:
    print(e)

from array import *
values = array('i',[25,14,63,85,3])
values.reverse()
newArray = array(values.typecode,(t*t for t in values))
for k in newArray:
    print(k)

from array import *
values = array('u',['y','t','h','d'])
for i in range(4):
    print(values[i])

from array import *
values = array ('u',['l','k','j','g'])
for y in values:
    print(y)

from array import *
values = array('i',[54,3,9,8])
newArray = array(values.typecode,(d*d for d in values))
i=0
while i<len(newArray):
    print(newArray[i])
    i=i+1