class Hello:
    def run(self):
        for i in range(5):
            print('Hello')
class Hi:
    def run(self):
        for i in range(5):
            print('Hi')
t1=Hello() #t1 is object and Hello() is constructor class
t2=Hi()    #t2 is object and Hi() is constructor class
t1.run()   #we are calling run method using object t1
t2.run()   #we are calling run method using object t2

output:
Hello
Hello
Hello
Hello
Hello
Hi
Hi
Hi
Hi
Hi
--------------------------------------------------------------------------------------------------------
from threading import * #we are importing everything from the threading package/module
class Hello(Thread):  #Hello class is the sub class of Thread class. #To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(500):
            print('Hello')
class Hi(Thread):  #Hi class is the sub class of Thread class.#To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(500):
            print('Hi')
t1=Hello() #t1 is object and Hello() is constructor class
t2=Hi()    #t2 is object and Hi() is constructor class
t1.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method
t2.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method

output: 
Hello
Hello
Hello
Hello
HelloHi

Hi
Hi
Hello
Hello
Hi
Hi
Hi
HelloHi
Hi
Hello
Hello
Hello
Hi

Hi
HiHello
Hello
Hello

Hello
Hi
HiHello

Hi
Hi
HiHello
Hi
Hello
Hello
Hello
Hi
Hi
Hello
Hello
Hello
Hi
Hi
Hi
Hi
Hi
Hi
.
.
.
.
#Its happening in parallel but the system is so fast that it executing at the same point,
 its a collision plus, In our system we have a concept of schedulers which will give us some 
 time to execute.
#We are expecting it will print only one hello in that particular time but its executing 10 times 
 in that gap its printing 50 times in that gap, to increase the gap since its going very fast 
 we will make it sleep, we will make it slow down the way we do is by importing a 
 package 'from time import sleep'
-------------------------------------------------------------------------------------------------------
from time import sleep  #to slow down the printing values and increase the gap, we are importing sleep module
from threading import *  #we are importing everything from the threading package/module
class Hello(Thread):  #Hello class is the sub class of Thread class. #To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(500):
            print('Hello')
            sleep(1)  #sleep for 1 second
class Hi(Thread):  #Hi class is the sub class of Thread class.#To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(500):
            print('Hi')
            sleep(1)  #sleep for 1 second
t1=Hello()  #t1 is object and Hello() is constructor class
t2=Hi()     #t2 is object and Hi() is constructor class
t1.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method
t2.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method

output:
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
.
.
.
.
#Its happening in parallel but the system is so fast that it executing at the same point,
 its a collision plus, In our system we have a concept of schedulers which will give us some 
 time to execute.
#We are expecting it will print only one hello in that particular time but its executing 10 times 
 in that gap its printing 50 times in that gap, to increase the gap since its going very fast 
 we will make it sleep, we will make it slow down the way we do is by importing a 
 package 'from time import sleep'
----------------------------------------------------------------------------------------------------------
from time import sleep #to slow down the printing values and increase the gap, we are importing sleep module
from threading import * #we are importing everything from the threading package/module
class Hello(Thread):  #Hello class is the sub class of Thread class. #To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(500):
            print('Hello')
            sleep(1)  #sleep for 1 second
class Hi(Thread):  #Hi class is the sub class of Thread class.#To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(500):
            print('Hi')
            sleep(1)  #sleep for 1 second
t1=Hello()  #t1 is object and Hello() is constructor class
t2=Hi()     #t2 is object and Hi() is constructor class
t1.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method
sleep(0.2) #0.2 seconds they shouldn't collide each other, so two different threads executes parallelly without any collision
t2.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method

output:
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
.
.
.
.
#Its happening in parallel but the system is so fast that it executing at the same point,
 its a collision plus, In our system we have a concept of schedulers which will give us some 
 time to execute.
#We are expecting it will print only one hello in that particular time but its executing 10 times 
 in that gap its printing 50 times in that gap, to increase the gap since its going very fast 
 we will make it sleep, we will make it slow down the way we do is by importing a 
 package 'from time import sleep'
--------------------------------------------------------------------------------------------------------
from time import sleep  #to slow down the printing values and increase the gap, we are importing sleep module
from threading import *  #we are importing everything from the threading package/module
class Hello(Thread):  #Hello class is the sub class of Thread class. #To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)  #sleep for 1 second
class Hi(Thread):  #Hi class is the sub class of Thread class.#To use two different threads we written Thread sub class for Hello & Hi classes
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)  #sleep for 1 second
t1=Hello() #t1 is object and Hello() is constructor class
t2=Hi()    #t2 is object and Hi() is constructor class
t1.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method
sleep(0.2) #0.2 seconds they shouldn't collide each other, so two different threads executes parallelly without any collision
t2.start() #if we want to create two different thread, instead of calling run() method we need to call start() method. #But internally it calls run() method
t1.join()  #t1&t2 object statements executes first parallely , at the last print statement executes
t2.join()  #t1&t2 object statements executes first parallely , at the last print statement executes
print('Bye')

output:
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Bye
-------------------------------------------------------------------------------------------------------
-when we break down the big task into small parts, each part will be called as thread.
-By default every execution has one thread, Even if we are not getting thread by ourself
 we do have one thread and that thread is known as Main thread
-we have main thread by default and main thread will execute all the statements

t1 & t2 are in the main thread
The moment it start it creats a new thread.
so, in total we are getting three threads
Those are 
1.Main Thread
2.t1 Thread
3.t2 Thread