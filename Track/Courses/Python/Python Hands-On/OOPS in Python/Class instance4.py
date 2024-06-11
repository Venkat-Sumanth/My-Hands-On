class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
person = person ("sumanth",24,'male')
print(person.name)
print(person.age)
print(person.gender)

output:
sumanth
24
male
---------------------------------------------------------------------------------------------------------------
-In Python, a class instance is an object that belongs to a class. 
-When we create a new instance of a class, you are creating a new object that has all of the same 
 attributes and methods as the class. 
-However, the values of the attributes may be different for each instance.
-For example, you could create a class called Person with attributes for name, age, and gender. 
 You could then create instances of the Person class to represent different people. 
 Each instance would have its own values for the name, age, and gender attributes.