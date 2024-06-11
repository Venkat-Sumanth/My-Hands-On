a=5
b=2
print(a/b)
print('bye')

output:
2.5
bye
-------------------------------------------------------------------------------------------------------
a=5
b=0
print(a/b)
print('bye')

output:
ZeroDivisionError: division by zero
#Here 0 cannot divisible by any value.Hence, its throwing an ZeroDivisionError error.
--------------------------------------------------------------------------------------------------------
a=5
b=0
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print(a/b) #its now a critical statement, so thats why we are using try keyword to execute
except Exception: #This line will handle the error still if the error left. #This block only will execute when we have an error
 print('Hey, you cannot divide a number by zero')
 print('bye')

output:
Hey, you cannot divide a number by zero
bye
--------------------------------------------------------------------------------------------------------
a=5
b=2
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print(a/b)
except Exception: #This block will not execute because there is no error
    print('Hey, you cannot divide a number by zero')
    print('bye')

output:
2.5
#Here there is no error thats why exception is not required, so its executed in the try block itself
--------------------------------------------------------------------------------------------------------
a=5
b=0
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print(a/b) #its now a critical statement, so thats why we are using try keyword to execute
except Exception as e: #This line will handle the error still if the error left. #This block only will execute when we have an error
    print('Hey, you cannot divide a number by zero',e)
    print('bye')

output:
Hey, you cannot divide a number by zero division by zero
bye
#Here there is an ZeroDivisionError thats why try block unable to execute then it jumps to Exception block , Exception block executes the output
--------------------------------------------------------------------------------------------------------
a=5
b=2
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('resource open')
    print(a/b) 
    print('resource close')
except Exception as e:
    print('Hey, you cannot divide a number by zero',e)
    
output:
resource open
2.5
resource close
#Here there is no error thats why it executes in try block itself
--------------------------------------------------------------------------------------------------------
a=5
b=0
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('resource open')
    print(a/b) #Here we are getting exception because 0 cannot divisible, then it jumps to exception block to execute the output
    print('resource close') #Because of the exception this print statement cannot execute
except Exception as e:
    print('Hey, you cannot divide a number by zero',e)
    
output:
resource open
Hey, you cannot divide a number by zero division by zero
--------------------------------------------------------------------------------------------------------
a=5
b=0
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('reource open')
    print(a/b) #Here we are getting exception because 0 cannot divisible #Hence it cannot execute because of exception. Immediately it goes to the exception block and then in the exception block statements executes
except Exception as e: 
    print('Hey, you cannot divide a number by zero',e)
    print('resource close')

output:
reource open
Hey, you cannot divide a number by zero division by zero
resource close
#Here because of ZeroDivisionError the execution jumps from try block to exception block
--------------------------------------------------------------------------------------------------------
a=5
b=2
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('resource open')
    print(a/b) #Here we didn't get any exception or error.it executes properly. so, that's why it didn't go to exception block hence we don't have any exception.
except Exception as e:
    print('Hey, you cannot divide a number by zero',e)
    print('resource close')

output:
resource open
2.5
#Here there is no error thats why it executes in try block itself
--------------------------------------------------------------------------------------------------------
a=5
b=2
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('resource open')
    print(a/b)
except Exception as e:
    print('Hey, you cannot divide a number by zero',e)
finally: #Finally block will be executed if we get error as well as if we don't get an error.
    print('resouce close')

output:
resource open
2.5
resouce close
#Here there is no error thats why it executes in try block itself
--------------------------------------------------------------------------------------------------------
a=5
b=2
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('resource open')
    print(a/b)
    k=int(input('Enter a number'))
    print(k)
except Exception as e:
    print('Hey, you cannot divide a number by zero',e)
finally: #Finally block will be executed if we get error as well as if we don't get an error.
    print('resource close')

output:
resource open
2.5
Enter a number5 #Here we entered the value 5
5
resource close
#Here there is no ZeroDivisionError, it executes in try block itself
--------------------------------------------------------------------------------------------------------
a=5
b=2
k = int(input('Enter a number')) #here we defined out of the try block . so its giving value error
print(k)
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('resource open')
    print(a/b)
except Exception as e:
    print('Hey, you cannot divide a number by zero',e)
finally: #Finally block will be executed if we get error as well as if we don't get an error.
    print('resource close')

output:
Enter a numberp #Here we entered value p
ValueError: invalid literal for int() with base 10: 'p'
--------------------------------------------------------------------------------------------------------
a=5
b=2
try: #try is statement, its try block #Try tries to execute, if it fails then 'except Exception' line will handle the error
    print('resource open')
    print(a/b)
    k=int(input('Enter a number'))
    print(k)
except ZeroDivisionError as e: #we written exception for ZeroDivisionError to not to throw any error
    print('Hey, you cannot divide a number by zero',e)
except ValueError as e:  #we written exception for ValueError to not to throw any error
    print('Invalid input')
except Exception as e: #Exception tries to handles all the errors which are like ZeroDivisionError & ValueError
    print('something went wrong....')
finally: #Finally block will be executed if we get error as well as if we don't get an error.
    print('resource close')
    
output:
resource open
2.5
Enter a numberp #Here we entered value p
Invalid input
resource close
#Here we have given an character datatype value, instead to give integer value but it executed and didnt thrown any error
--------------------------------------------------------------------------------------------------------
1)Compile time error
2)Logical error
3)Run time error

1)Compile time error:
Cases:
1.suppose if we are working with 'if' and if we forgot to write column (:)
2.if we are writing print statement and if the print spelling is wrong
  The above two cases are syntactical errors, we can call them as compile time error because 
  we will be reading those errors at compile time.
  
2)Logical error:
-Lets say our code is working, nothing wrong with the syntax, everything is working.
Case:
-when the user says I want to add two numbers.
 2+3=5 but the user is getting 2+3=4, so this is a logical error
 Logical error, code gets compiled and code also gives the output but the problem is its not 
 the correct output. That's the logical error.

3)Run time error:
-In run time error code gets compiled and there is no syntactical error and our code is not 
 giving any logical error as well, everything is working
-sometimes user might give a wrong input
-Example, lets say we want to divide two numbers i.e, 5/6 both the values are coming from user.
-if the user says 6/2=3 .it gives 3 as output
-if the user says 10/5=2. it gives 2 as output
-what, if the user says 6/0 we cannot divide number by 0 that's where it gives an error, 
 its not an compile time error its getting compiled properly
 its not a logical error, for normal execution it works.
 its not working for specific input, our code was working but somewhere in between 
 we are getting error that's run time error, because we are getting error at run time





