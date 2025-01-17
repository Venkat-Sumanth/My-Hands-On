class Parent(object):
    pass
class child(Parent):
    pass
print(issubclass(child,Parent))
print(issubclass(Parent,child))

class child:
    pass
class parent:
    pass
obj1=child()
obj2=parent()
print(isinstance(obj1, child))
print(isinstance(obj2, parent))
print(isinstance(obj1, parent))
print(isinstance(obj2, child))


class InterviewbitEmployee:
    def __init__(self,emp_name):
        self.emp_name = emp_name
    def introduce(self):
        print('Hello, I am ',self.emp_name)
emp = InterviewbitEmployee('Mr Employee')
emp.introduce()

class Animal:
    def speak(self):
        return "some generic sound"
class Dog(Animal):
    def speak(self):
        return "woof! woof"
generic_animal = Animal()
print(generic_animal.speak())
dog = Dog()
print(dog.speak())

class Animal(object):
    def speak(self):
        return "some generic sound"
class Dog:
    def speak(Animal):
        return "woof! woof!"
generic_animal = Animal()
print(generic_animal.speak())
dog = Dog()
print(dog.speak())


class Animal(object):
    def speak(self):
        return "some generic sound"
class Dog(Animal):
    def speak(self):
        base_sound = super().speak()
        return(f"{base_sound},Specifically woof! woof!")
dog = Dog()
print(dog.speak())

class EmptyClassDemo:
    pass
obj = EmptyClassDemo()
obj.name = "Interviewbit"
print("Name Created=", obj.name)


class BaseClass:
    def instance_method(self):
        return "Base instance method"
    @classmethod
    def class_method(cls):
        return "Base class method"
    @staticmethod
    def static_method():
        return "Base static method"
class Derivedclass(BaseClass):
    def instance_method(self):
        return "derived instance method"
Base_instance = BaseClass()
Derived_instance = Derivedclass()
print(Base_instance.instance_method())
print(Derived_instance.instance_method())

print(BaseClass.class_method())
print(Derivedclass.class_method())

print(BaseClass.static_method())
print(Derivedclass.static_method())


class BaseClass():
    def __init__(self):
        self.public_var ="I am a public variable"
        self._protected_var = "I am a protecetd variable"
        self.__private_var = "I am  a private variable"

    def public_method(self):
        return "I am a public method"

    def _protected_method(self):
        return "I am a protected method"

    def __private_method(self):
        return "I am a private method"

    def access_private_method(self):
        return self.__private_method()

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()

    def access_protected_method(self):
        return self._protected_method()

    def access_private_method_from_base(self):
        return self.access_private_method()

base_instance = BaseClass()
derived_instance = DerivedClass()

print(base_instance.public_var)
print(base_instance.public_method())

print(base_instance._protected_var)
print(derived_instance._protected_method())

print(base_instance.access_private_method())
print(derived_instance.access_private_method_from_base())


class Parent(object):
    def __init__(self,name):
        self.name = name
class child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def display(self):
        print(self.name,self.age)
obj = child('Interviewbit',26)
obj.display()


class Parent(object):
    def __init__(self,name):
        self.name = name
class child(Parent):
    def __init__(self,name,age):
        Parent.name = name
        self.age = age
    def display(self):
        print(Parent.name,self.age)
obj = child('Interviewbit', 52)
obj.display()


class ParentClass:
    def parent_function(self):
        print("I am parent calss function")
class childclass(ParentClass):
    def child_function(self):
        print("I am child class function")
obj1 = childclass()
obj1.parent_function()
obj1.child_function()


class A:
    def __init__(self,a_name):
        self.a_name =a_name
class B(A):
    def __init__(self,b_name,a_name):
        self.b_name = b_name
        A.__init__(self,a_name)
class C(B):
    def __init__(self,c_name,b_name,a_name):
        self.c_name = c_name
        B.__init__(self,b_name,a_name)

    def display_names(self):
        print("A name:",self.a_name)
        print("B name:",self.b_name)
        print("C name",self.c_name)
obj1 = C("child","intermediate","Parent")
print(obj1.a_name)
obj1.display_names()


class Parent1:
    def parent1_function(self):
        print("I am first parent")
class Parent2:
    def parent2_function(self):
        print("I am second parent")
class child(Parent1,Parent2):
    def child_function(self):
        self.parent1_function()
        self.parent2_function()
obj1 = child()
obj1.child_function()


class A:
    def a_function(self):
        print("I am from the parent class")

class B(A):
    def b_function(self):
        print("I am from first child")

class C(A):
    def c_function(self):
        print("I am from second class")
obj1 = B()
obj2 = C()
obj1.a_function()
obj1.b_function()
obj2.a_function()
obj2.c_function()


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name},Age: {self.age}")
person1 = Person("sumanth",24)
person1.display()
person2 = Person('suma',33)
person2.display()


import array as arr
numbers = arr.array('i',[1,2,3,4,5])
print("Array elements")
for num in numbers:
    print(num)
numbers.append(6)
print("\nArray after appending 6:")
print(numbers)
numbers.remove(3)
print("\nArray after removing 3:")
print(numbers)
print("\nElement at index 2:", numbers[2])
numbers[2] = 10
print("\nArray after modifying element at index 2:")
print(numbers)


numbers = [1,2,3,4,5]
print("List of elements:")
for num in numbers:
    print(num)
numbers.append(6)
print("\nLists after appending 6:")
print(numbers)
numbers.remove(3)
print("\nList after removing 3:")
print(numbers)
print("\nElement at index 2:", numbers[2])
numbers[2] = 10
print("\nList after modifying element at index 2:")
print(numbers)

numbers = [0,1,2,3,4,5,6,7,8,9]
print("Original list:", numbers)
slice1 = numbers[2:6]
print("slice from index 2 to 5:", slice1)
slice2 = numbers[:6]
print("slice from start to index 5:", slice2)
slice3 = numbers[4:]
print("slice from index 4 to end:", slice3)
slice4 = numbers[1:8:2]
print("slice from index 1 to 7 with step 2:", slice4)
slice5 = numbers[-5:-1]
print("slice with negative indeces (-5 to -1):", slice5)
slice6 = numbers[::-1]
print("Reverse the list:", slice6)
partial_slice = numbers[::2]
print("slice every second element from the list:", partial_slice)




def example_function(param1, param2):
    """
    This is an example function.

    Parameters:
     param1(int): The first parameter.
     param2(str): The second parameter.

     Returns:
        str: A formatted string combining param1 and param2.
    """
    return f"{param1} - {param2}"
class ExampleClass:
    """
    This is an example class

    Attributes:
    attribute1(int) : The first attribute.
    attribute2(str) : The second attribute
    """
    def  __init__(self,attribute1,attribute2):
         """
        The constructor for ExampleClass

         parameters:
         attribute1(int): The first attribute
         attribute2(str): The second attribute
         """
         self.attribute1 = attribute1
         self.attribute2 = attribute2
    def method_example(self,param):
        """
        An example method

        Parameters:
        param(int): A parameter for the method.

        Returns:
        str: A string stating the value of the parameter.
        """
print(example_function.__doc__)
print(ExampleClass.__doc__)
print(ExampleClass.__init__.__doc__)
print(ExampleClass.method_example.__doc__)


for i in range(1,3):
    if i==3:
        break
    print(i)


for i in range(1,6):
    if i==3:
        continue
    print(i)


for i in range(1,6):
    if i==3:
        pass
    else:
        print(i)



























