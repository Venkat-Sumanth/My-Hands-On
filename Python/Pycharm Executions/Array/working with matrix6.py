from numpy import *
arr1=array([
              [1,2,3],
               [4,5,6]
])
print(arr1.dtype)  #dtype(Attribute of numpy package).It returns the datatype of an array

output:
int32
------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
              [10,20,30],
               [40,50,60]
])
print(arr1.ndim) #ndim(Attribute of numpy package).Its returns the number od dimension array.

output:
2
--------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1 = array([
                [2,3,5,8],
                 [4,3,87,32]
])
print(arr1.shape) #shape(Attribute of numpy package).It returns the no.of rows and no.of values in rows. 

output:
(2, 4)   #2 is no.of rows and 4 is no.of values in a row.
--------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
            [1,2,3,4],
             [3,4,5,5]
])
print(arr1.size)   #size(Attribute of numpy package).It returns the size number of values in rows

output:
8
--------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
             [2,3,4,5],
              [4,5,6,7] #2d array
])
arr2=arr1.flatten()  #flatten() function is method provided by numpy library.
print(arr2)

output:
[2 3 4 5 4 5 6 7] #1d array
#Flatten() method is used to convert 2d array to 1d array
----------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
             [2,3,4,5,3,5],
              [4,5,6,7,2,4]
])
arr2=arr1.flatten()
arr3=arr2.reshape(3,4)  #reshape() is function in numpy library.#reshape(3,4)_3 is no.of rows and 4 is no.of values in rows.
print(arr3)

output:
[[2 3 4 5]
 [3 5 4 5]
 [6 7 2 4]]
 #reshape() allows to change the dimensions of the array without affecting the data it contains.
---------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
             [1,2,3,4,5,6],
              [7,8,9,10,11,12]
])
arr2=arr1.flatten()
arr3=arr2.reshape(2,2,3) #2 is no.of rows in 2d, 2 is no.of rows in 2d_3 is no.of values in a row.
print(arr3)

output:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
-----------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
             [2,3,4,5,6,7],
              [4,5,6,7,4,5]
])
m=matrix(arr1)
print(m)

output:
[[2 3 4 5 6 7]
 [4 5 6 7 4 5]]
#Matrix is a data structure that is used to represent two-dimensional arrays. 
#In Python, matrices are typically represented as lists of lists.
 --------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
            [20,30,40,60],
             [31,32,63,45]
])
m=matrix('20 30 40 60 ; 31 32 63 45')
print(m)

output:
[[20 30 40 60]
 [31 32 63 45]]
--------------------------------------------------------------------------------------------------------------------
from numpy import *
arr1=array([
             [12,13,14,15,16,17],
              [12,14,15,13,15,12]
])
m=matrix('12 13 14 ; 15  16 17 ; 18 32 12 ; 14  15 13 ; 15 12  18')
print(m)

output:
[[12 13 14]
 [15 16 17]
 [18 32 12]
 [14 15 13]
 [15 12 18]]
-------------------------------------------------------------------------------------------------------------------
from numpy import *
m=matrix('12 13 14 ; 15  16 17 ; 18 32 12')
print(diagonal(m)) #diagonal() is function in numpy library.

output:
[12 16 12]
#diagonal() returns the diagonal elements in an array.
----------------------------------------------------------------------------------------------------------------------
from numpy import *
m=matrix('12 13 14 ; 15  16 17 ; 18 32 12 ; 14  15 13 ; 15 12  18')
print(m.min()) #min() is function.It returns min element in an array.

output:
12
----------------------------------------------------------------------------------------------------------------------
from numpy import *
m=matrix('12 13 14 ; 15  16 17 ; 18 32 12 ; 14  15 13 ; 15 12  18')
print(m.max()) #max() is function.It returns max element in an array.

output:
32
---------------------------------------------------------------------------------------------------------------------
from numpy import *
m1=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m3=m1+m2
print(m3)

output:
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
 -------------------------------------------------------------------------------------------------------------------
from numpy import *
m1=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m3=m1*m2
print(m3)

output:
[[ 30  36  42]
 [ 66  81  96]
 [102 126 150]]
 ------------------------------------------------------------------------------------------------------------------
 - If a list contains multiple elements of the same type, then it is known as an array.
- When an array contains another array inside it, then it is known as a two-dimensional array.
- Two- dimensional array can be defined as an array within another array. 
- It is a collection of rows and columns.

Syntax of a two-dimensional array:-
arr= array([
   [arr1],
   [arr2]
  ])
  
- Matrices can be defined as a two-dimensional array that has multiple rows and columns.
- A matrix that has one row and multiple columns is known as a row matrix.
-  A matrix having one column and multiple rows is known as a column matrix.
- Both the row matrix and column matrix is in the form of a single-dimensional array.
- A separate format available for a matrix in python.