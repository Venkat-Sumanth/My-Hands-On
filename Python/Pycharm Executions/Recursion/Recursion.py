def greet():
    print("Hello")
    greet()         #Here function calling itself . so thats why its recursion
greet()             #we are calling the function to execute

output:
Hello
Hello
Hello
  .
  .
  .
Hello #it continues to 996 times #max recursion limit is 1000 times.
---------------------------------------------------------------------------------------------------------------------
import sys                    #sys is module/Library
print(sys.getrecursionlimit()) #getrecursionlimit() is method and it gives the recursion limit.#It means how many times 'hello' is printing.
def greet():
    print("Hello")
    greet()                   #we are calling the function in the function
    
output:
1000
----------------------------------------------------------------------------------------------------------------------
import sys                          #sys is module/Library
print(sys.setrecursionlimit(2000))  #setrecursionlimit(2000) is method and we passing the limit 2000 in it.#Its used to set the limit number.
print(sys.getrecursionlimit())      #getrecursionlimit() is method and it gives the recursion limit.#It means how many times 'hello' is printing.
i=0                                 #we are initializing i=0 and its outside of the function so it is global variable.
def greet():
    global i                        #global is keyword so it considers 'i' as a global variable inside the function.
    i+=1                            #This line increments till the limit reaches 2000
    print('hello',i)                #In print satement 'i' is written to print the recursion incremented number sequence to reach the limit 2000.
    greet()                         ##we are calling the function in the function beacuse its recursion.
greet()                             #we are calling the function to execute

output:

None
2000
hello 1
hello 2
hello 3
hello 4
   .
   .
   .
hello 1998
hello 1999 #As limit is 2000.
-----------------------------------------------------------------------------------------------------------------------
- Recursion means calling a function from itself.
- To print a statement of a function multiple times, we can call a function inside the same function.
- By default, a function inside a function will execute infinite times.
- Maximum limit for recursion is 1000 in python, so it will give an error after exceeding its limit.
- Limit can also be changed by doing some customization.
- If a code goes into recursion without a condition and it goes to infinite times, then it may hang the system and that limit is set in python.
- We can also print the limit of recursion by using the function getrecursionlimit() available in the sys library.
- We can change the limit for a recursion by using the setrecursionlimit() function.
- We can set the limit to any number by providing it in the setrecursionlimit() method.
- We have to make the variable global to access it if it is defined outside the scope.
- Recursion is used to perform several tasks in many projects.

- A complicated function can be split down into smaller sub-problems by using the recursion.
- Recursive functions make the code look simple and effective.
