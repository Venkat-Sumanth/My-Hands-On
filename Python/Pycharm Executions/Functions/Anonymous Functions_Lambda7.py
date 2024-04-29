def square(a):
    return a*a
result = square(4)       #we are calling the function to execute
print(result)

output:
16
----------------------------------------------------------------------------------------------------------------------
#instaed of defining function we can write the function by writing lambda function.
f=lambda a:a*a  #Here 'f' is function(variable).#lambda is function/lambda expression.#Here 'a' is argument we are passing and 'a*a' is operation we are doing.Before colon(:) is argument we are passing, after colon(:) is operation we are doing. 
result=f(4)
print(result)

output:
16
--------------------------------------------------------------------------------------------------------------------
f=lambda a,b:a+b #Before colon(:) is argument we are passing, after colon(:) is operation we are doing
result=f(5,6)
print(result)

output:
11
----------------------------------------------------------------------------------------------------------------------
- Normal functions are defined by using the def keyword and function name.
- A function without a function name is known as an Anonymous function.
- Anonymous function is called a lambda function.
- Functions are objects in Python so we can also pass a function in a function.
- Instead of defining a function, we can directly define it whenever it is required to use.
- We have to use the lambda keyword to directly define the function in one line.
- We need to store the lambda function in a variable as the function is also an object.
- Then, that variable will define the function and we can also use it in other functions.
- We can pass any number of arguments in a lambda function but it should be only one expression.
- Lambda functions are syntactically restricted to a single expression.

Advantages of Lambda Function:-
- Lambda function supports single-line statements that return some value.
- It is useful when we have to perform short operations and data manipulations.
- It saves the time as it requires less time to read the code.