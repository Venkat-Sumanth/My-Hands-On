print("Hello")

output:
Hello
---------------------------------------------------------------------------------------------------------------
print("Hello " + __name__) #it prints '__main__' in '__name__' place because here we running calc 

output:
Hello __main__
--------------------------------------------------------------------------------------------------------------
import demo #As we imported 'demo'. it prints all the print functions in 'demo' with 'calc'.
print("its time to calculate")

output:
Hello
welcome user
its time to calculate
--------------------------------------------------------------------------------------------------------------
import demo 
print("its time to calculate")

output:
its time to calculate
#Now it prints only print function of 'calc' only because we defined the 'demo' print functions as below.

#The below code is taken from 'demo'. 
def main():
    print("Hello")
    print("welcome user")
main()         #we are calling the function to execute.

output:
Hello
welcome user
---------------------------------------------------------------------------------------------------------------
