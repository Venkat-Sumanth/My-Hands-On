def update(x):      #update() is function
    x=8
    print("x ",x)
a=10
update(a)
print("a ",a)

output:
x  8
a  10
------------------------------------------------------------------------------------------------------------------
def update(x):
    print(id(8))
    x=8
    print(id(x))
    print("x ",x)
a=10
print(id(a))
update(a)
print("a ",a)

output:
140719647541976
140719647541912
140719647541912
x  8
a  10
----------------------------------------------------------------------------------------------------------------------
def update(list):
    print(id(list))
    list[1] = 25
    print(id(list))
    print("x ",list)
list = [10,20,30]
print(id(list))
update(list)
print("list ",list)

output:
2443343679744
2443343679744
2443343679744
x  [10, 25, 30]
list  [10, 25, 30]
----------------------------------------------------------------------------------------------------------------------
-All variables are actually references to objects in memory. 
 Thus, when a function is called with a parameter, the reference to the object is passed by value.
 
-For immutable data types like integers, floats, and strings, changes made to the parameter inside the 
 function do not affect the original value of the parameter outside the function. 
 This is because any changes made to the parameter create a new object in memory, 
 and the original reference to the object remains unchanged. 

-For mutable data types like lists and dictionaries, changes made to the parameter inside the 
 function do affect the original value of the parameter outside the function. 
 This is because the reference to the object remains the same, but the contents of the object can be modified.
 -------------------------------------------------------------------------------------------------------------------
 def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print("x",lst)
lst = [10,20,30]
print(id(lst))
update(lst)
print(lst)
---------------------------------------------------------------------------------------------------------------------
-The above code defines a Python function called update that takes a list lst as a parameter. 
 The function first prints the memory address of the list using the id() function. 
 It then modifies the second element of the list by assigning it the value 25. 
 The function then prints the new memory address of the list and the updated list.
 
-The code then creates a list called lst with the values [10, 20, 30] and prints its memory address using 
 the id() function. The update function is then called with the lst parameter. 
 Since lists are mutable objects in Python, the memory address of the list is passed to the function, 
 making it a pass by reference.
 
-Inside the update function, the second element of the list is modified to 25. 
 Since lists are mutable objects and the memory address of the original list is passed to the function, 
 this change affects the original list outside the function. The new memory address and the 
 updated list are printed inside the function.
--------------------------------------------------------------------------------------------------------------------
-Pass by value:
 (creation of another container with the same value ---> now we have 2 containers with the same value ----> they are 
 independent of each other, changing the value inside one container does not change the value inside the 
 other container)Value is passed, resulting in 2 separate locations in the memory storing the same value. 
 Therefore, a change in the 'copied' value will not affect the original value because they are 
 inhabiting separate memory locations.
 
-Pass by reference:
 (There is no creation of a new container, this is just aliasing)
 Pointing the function to the memory location of the data/value you are passing. 
 In other words, no copying of values are actually taking place. 
 So there really is only one memory location storing one value. 
 This is basically aliasing. So a change in one of the aliases will obviously affect the value 
 of the other aliases because they are the same thing.
 
-In Python:
 When you pass a variable with its value into a function, if its value is not changed by the function, 
 reference (physical location / address on memory) is not changed. 
 So at this point, there is no creation of a new memory (container). 
 But as soon as the function changes the value of the argument, a new memory is created, 
 so now you have 2 containers holding different values. 
 But this is only for immutable (cannot be mutated/modified/changed) datatypes like integers and strings. 
 But if you pass in a mutable datatype like a list into the function and change its value, 
 since it is mutable, the data can be updated/changed in-situ (without the creation of a new memory). 
 This results in still just one memory location, but with an updated value stored in it.

-Just to clear the confusion:  
 In the first example, value of 'a' did not get updated because the types int and string are immutable. 
 In the 2nd example, sir used LIST which is mutable, therefore the values outside the function also got changed.