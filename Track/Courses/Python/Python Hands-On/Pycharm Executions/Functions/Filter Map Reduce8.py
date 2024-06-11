Generic defining of filter function:
def is_even(n):              #Here we are directly defining function 
    return n%2==0            #we are written the condition to return the values to the code.
nums=[3,2,6,8,4,6,2,9]       #we are passing values to the list
evens = list(filter(is_even,nums)) #evens is variable that hold the filter function.
print(evens)

output:
[2, 6, 8, 4, 6, 2]
-----------------------------------------------
Filter Function:
The filter() function in Python is used to filter out elements from an iterable 
(such as a list, tuple, or set) based on a given condition. 
The function takes two arguments: 
1.function(which and where we mention the logic) and 
2.Iterable(sequence).
--The syntax for the filter() function is:
filter(function, iterable)

Ex:
nums=[3,2,6,8,4,6,2,9]             #we are passing values to the list
evens = list(filter(lambda n : n%2==0,nums)) #Instaed of defining normal function on the top we are writing the lambda function/lambda expression in a single line to return the values to the code.#Before colon(:) is argument we are passing, after colon(:) is operation we are doing
print(evens)       #Printing the evens variable which evens variable holds filter function.

output:
[2, 6, 8, 4, 6, 2]
#Filter() is built-in function.
----------------------------------------------------------------------------------------------------------------------
Map Function:
The map() function in Python is a built-in function that allows you to apply a function to each item 
in an iterable (like a list or dictionary) and return a new iterator for retrieving the results.
--The syntax for the map() function is:
map(function, iterable)

Ex:
nums = [3,2,6,8,4,6,2,9]           #we are passing values to the list
evens = list(filter(lambda n:n%2==0,nums)) #Instaed of defining normal function on the top we are writing the lambda function/lambda expression in a single line to return the values to the code.#Before colon(:) is argument we are passing, after colon(:) is operation we are doing
doubles = list(map(lambda n:n*2,evens))  #Instaed of defining normal function on the top we are writing the lambda function/lambda expression in a single line to return the values to the code for map function.#Before colon(:) is argument we are passing, after colon(:) is operation we are doing.
print(doubles)

output:
[4, 12, 16, 8, 12, 4]
#Map() is built-in function.
----------------------------------------------------------------------------------------------------------------------
Reduce Function:
reduce() is a function that implements a mathematical technique called folding or reduction. 
reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.
--The syntax for the reduce() function is:
functools.reduce(function, iterable[, initializer])
 
Ex:
from functools import reduce  #Here we imported reduce() through functools. Then only reduce() works.
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n:n%2==0,nums)) #Instaed of defining normal function on the top we are writing the lambda function/lambda expression in a single line to return the values to the code.#Before colon(:) is argument we are passing, after colon(:) is operation we are doing
doubles = list(map(lambda n:n*2,evens)) #Instaed of defining normal function on the top we are writing the lambda function/lambda expression in a single line to return the values to the code for map function.#Before colon(:) is argument we are passing, after colon(:) is operation we are doing
print(doubles)
sum = reduce(lambda a,b:a+b,doubles) #Instaed of defining normal function on the top we are writing the lambda function/lambda expression in a single line to return the values to the code for reduce function.#Before colon(:) is argument we are passing, after colon(:) is operation we are doing.
print(sum) #Here we are adding value one-by-one . so we written sum as a variable.

output:
[4, 12, 16, 8, 12, 4]
56
#Reduce() is built-in function.
----------------------------------------------------------------------------------------------------------------------
- Lambda function can be used with these three functions:
1. filter()
2. map()
3. reduce()

- filter() function will take a list and do filtering and give values.
- filter() takes a sequence and also returns a sequence.
- filter() function takes two arguments: function and iterable.
  -> filter(func, iterable)
- We have to give the definition of a function that we have passed as a condition in an argument.
- The defined function should return a value of either True or False based on the condition.
- Then, filter() will take the value that is returned by the defined function and does perform filtering based 
  on this value.
- In the defined function, we need only two things i.e, a variable and an expression. So, we can also use the 
  lambda function instead of using the normal function to define the condition for a filter.
-Lambda reduces the number of lines of code and makes it more precise.
- Filter() simply returns the iterable passed to it. 

- map() function is used when we want to change the value of every element of a list.
- map() function also takes two arguments i.e., a function and an iterable.
  -> map(func, *iterables)
-  To get the result as a list, the built-in list() function can be called on the map object.
- We have to define a function that we have passed as a condition in an argument.
- The defined function should return any value. 
- The lambda function can also be used in an argument as a function instead of defining the normal 
  function for the logic.
- map() function returns a list. The function returns a map object which is a generator object.

- reduce() function is used to reduce the number of values from a list.
- reduce() function belongs to a module known as functools.
- We have to import the module functools from the library to use the reduce function.
- reduce() also take two arguments i.e., a function and a sequence.
  -> reduce(func, iterable[, initial])
- We have to give the definition of a function that we have passed as a condition in an argument.
- The lambda function can also be used in an argument as a function instead of defining the normal 
  function for the logic.
