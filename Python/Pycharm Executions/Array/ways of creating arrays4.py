array():
from numpy import *
arr = array([1,2,3,4],float)
print(arr.dtype)            #dtype means datatype
print(arr)

output:
float64
[1. 2. 3. 4.]
________________________________
from numpy import *
arr=array([2,3,4,5],int)
print(arr.dtype)
print(arr)

output:
int32
[2 3 4 5]
#dtype is an object that describes the type of data that is stored in a NumPy array. 
 Dtypes are important because they allow NumPy to perform efficient operations on arrays
---------------------------------------------------------------------------------------------------------------------
linspace():
from numpy import *
arr = linspace(1,10,15)   #start is 1, end is 10, difference is 15
print(arr)

output:
[ 1.          1.64285714  2.28571429  2.92857143  3.57142857  4.21428571
  4.85714286  5.5         6.14285714  6.78571429  7.42857143  8.07142857
  8.71428571  9.35714286 10.        ]
#Linspace do line1 to line10 into 15 different parts
_______________________________________________________________________________
from numpy import *
arr = linspace(1,10)   #start is 1, end is 10_No difference is written . so it returns 10 different parts.
print(arr)

output:
[ 1.          1.18367347  1.36734694  1.55102041  1.73469388  1.91836735
  2.10204082  2.28571429  2.46938776  2.65306122  2.83673469  3.02040816
  3.20408163  3.3877551   3.57142857  3.75510204  3.93877551  4.12244898
  4.30612245  4.48979592  4.67346939  4.85714286  5.04081633  5.2244898
  5.40816327  5.59183673  5.7755102   5.95918367  6.14285714  6.32653061
  6.51020408  6.69387755  6.87755102  7.06122449  7.24489796  7.42857143
  7.6122449   7.79591837  7.97959184  8.16326531  8.34693878  8.53061224
  8.71428571  8.89795918  9.08163265  9.26530612  9.44897959  9.63265306
  9.81632653 10.        ]
#Here linspace do is prints 10 different parts.
---------------------------------------------------------------------------------------------------------------------
arange():
from numpy import *
arr = arange(1,20,2)
print(arr)

output:
[ 1  3  5  7  9 11 13 15 17 19]
------------------------------------------------------------------------------------------------------------------
logspace():
from numpy import *
arr = logspace(1,40,5)   #start is 1, end is 40, difference is 5
print(arr)

output:
[1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30
 1.00000000e+40]
#Here logspace do is it returns 5 different parts from log:1 to log:40
_________________________________________________________________________
from numpy import *
arr = logspace(2,50,7)
print('%.2f' %arr[6])

output:
100000000000000007629769841091887003294964970946560.00
#Here it prints the arr[0-6] values because defined number is 7.
#'e' is inclueded in fetched value. so to print 'e' in normal format we write '%.2f'.
#To fetch array value . we write index %arr[6].Here we can change index value from [0-6]
----------------------------------------------------------------------------------------------------------------------
Zeros():
from numpy import *
arr = zeros(5)
print(arr)

output:
[0. 0. 0. 0. 0.]
______________________________________________
from numpy import *
arr = zeros(6,int)
print(arr)

output:
[0 0 0 0 0 0]
---------------------------------------------------------------------------------------------------------------------
ones():
from numpy import *
arr=ones(5)
print(arr)

output:
[1. 1. 1. 1. 1.]
_________________________
from numpy import *
arr = ones(5,int)
print(arr)

output:
[1 1 1 1 1]
---------------------------------------------------------------------------------------------------------------------
Ways of creating arrays in numpy: 
   we have 6 way of creating arrays in numpy
    a)array()
    b)linspace()
    c)arange()
    d)logspace()
    e)zeros()
    f)ones()

