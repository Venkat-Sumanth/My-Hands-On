print(__name__)  #Here '__name__' is variable that returns the '__main__'   #'__main__' is the starting point of execution.

output:
__main__  #Here '__name__' returned '__main__' as the output
--------------------------------------------------------------------------------------------------------------
import calc  #Here we imported calc. so, everything will come to 'demo' from 'calc' including print function
print("Demo says : " +__name__) #As we imported the 'calc' the print function in 'calc' returned in 'demo' as 'Hello calc'. but it in the 'calc' it returns as 'Hello __main__' .Because in 'calc' we are running it. In demo we imported it.

output:
Hello calc
Demo says : __main__
--------------------------------------------------------------------------------------------------------------
print("Hello")
print("welcome user")

output:
Hello
welcome user
--------------------------------------------------------------------------------------------------------------
def main():
    print("Hello")
    print("welcome user")
main()         #we are calling the function to execute.

output:
Hello
welcome user
---------------------------------------------------------------------------------------------------------------
#we taken the below code from 'calc'
import demo #As we imported 'demo'. it prints all the print functions in 'demo' with 'calc'.
print("its time to calculate")

output:
Hello
welcome user
its time to calculate

#As the above code in 'calc' is printing the 'demo' print functions as we imported 'demo'.To avoid that we define(def) in a function as below follows.
def main():
    print("Hello")
    print("welcome user")
if __name__== "__main__": #This condition is written for 'if __name__== "__main__":' then only execute.
    main()
    
output:
Hello
welcome user
---------------------------------------------------------------------------------------------------------------
- _main_  is the starting point of the python. 
- The first module name is always main and the code starts from main.
- _name_ is a variable name that return the __main__.
- name_ is a built-in variable that evaluates the name of the current module.
- The value of the name changes as per the place where it is used, so that's why it is known as a variable.
- If you are an individual file or module, then the name will return main. 
- If you are importing another module containing the name variable in any file, then the name variable 
  will return the name of that module.
OR, 
- If you are running a file as a main and using a named variable in it, then it will print the main.
- But if you are printing a name that is imported as a module in another file, then it will 
  print the module name.
  

- The use of a function with the name variable helps the interpreter in checking if 
  it's parsing the currently executed script, or if it's temporarily parsing another external script. 
  
 if _name_ == "__main__":
This statement helps us to control the behaviour of different parts of the program.

- It chooses the number of lines of codes that can be executed from the external script as well 
  as the currently executed script depending on the scenarios.