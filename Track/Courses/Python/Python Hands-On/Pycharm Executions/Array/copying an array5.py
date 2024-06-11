from numpy import *
arr = array([1,2,3,10,6])
arr= arr+5
print(arr)

output:
[ 6  7  8 15 11]
------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1 = array([10,20,30,40,50])
arr2 = array([10,20,40,50,40])
arr3 = arr1+arr2
print(arr3)

output:
[20 40 70 90 90]
--------------------------------------------------------------------------------------------------------------------
from numpy import *
arr = array([4,5,6,1,2])
print(sin(arr))

output:
[-0.7568025  -0.95892427 -0.2794155   0.84147098  0.90929743]
------------------------------------------------------------------------------------------------------------------
from numpy import *
arr = array([33,22,42,64])
print(cos(arr))

output:
[-0.01327675 -0.99996083 -0.39998531  0.39185723]
------------------------------------------------------------------------------------------------------------------
from numpy import *
arr = array([10,65,32,47,85])
print(log(arr))

output:
[2.30258509 4.17438727 3.4657359  3.8501476  4.44265126]
-------------------------------------------------------------------------------------------------------------------
from numpy import *
arr = array([2,4,6,9,3])
print(sqrt(arr))

output:
[1.41421356 2.         2.44948974 3.         1.73205081]
---------------------------------------------------------------------------------------------------------------------
from numpy import *
arr = array([1,2,3,4,5])
print(sum(arr))

output:
15
------------------------------------------------------------------------------------------------------------------
from numpy import *
arr = array([21,32,63,45,1])
print(min(arr))

output:
1
------------------------------------------------------------------------------------------------------------------
from numpy import *
arr = array([20,30,14,52,1000])
print(max(arr))

output:
1000
------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1 = array([1,5,74,65,63])
arr2 = array([32,42,45,65])
print(concatenate([arr1,arr2]))

output:
[ 1  5 74 65 63 32 42 45 65]
---------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1 = array([10,32,45,64])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

output:
[10 32 45 64]
[10 32 45 64]
2063444071536
2063444071536
----------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1 = array([10,32,45,64])
arr2=arr1.view()            #view() function defines that array address changed into different address for both the arrays in the output.
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

output:
[10 32 45 64]
[10 32 45 64]
2011119605040
2011122514608
-----------------------------------------------------------------------------------------------------------------------
#shallow copy:              #Here the value what we replaced in arr1[1] that reflects to both arrays in output.
from numpy import *
arr1 = array([10,32,45,64])
arr2 = arr1.view()
arr1[1]= 8
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

output:
[10  8 45 64]
[10  8 45 64]
2148596176176
2148599085840
---------------------------------------------------------------------------------------------------------------------
#Deep copy:                  #Here the value what we replaced in arr1[1] that reflects to arr1[1] array in output.
from numpy import *
arr1 = array([10,32,45,64])
arr2 = arr1.copy()
arr1[1]= 8
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

output:
[10  8 45 64]
[10 32 45 64]
1961570981168
1961573890832
--------------------------------------------------------------------------------------------------------------------
- In python, two copying techniques are available i.e.,
1. Shallow Copy
2. Deep Copy
- In shallow copy, it will copy elements but it means both arrays are dependent on each other.
- In shallow copy, if we update an element in one array then the changes would also be reflected in another array.
- In a deep copy, two different arrays are not linked with each other in any way.
- In a deep copy, we use the function known as a copy() instead of using the view() function.
- copy() function provides a deep copy of an array.
