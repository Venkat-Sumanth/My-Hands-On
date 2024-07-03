class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1=Employee('venkata','sumanth',50000)
emp2=Employee('venu','suma',1600)

print(len(emp1))   #def __len__(self): -->method

print(len('test'))
print('test'.__len__())

print(emp1 + emp2)

print(emp1.__repr__())
print(emp1.__str__())

print(1+2)
print(int.__add__(1,2))
print(str.__add__('a','b'))

output:
15

4
4

51600

Employee('venkata', 'sumanth', '50000')
venkata sumanth - venkata.sumanth@email.com

3
3
ab


repr() Method:
The Python repr() method is mostly used for the purpose of debugging and development. 
The Python repr() built-in function returns the printable representation of the specified object as a string.

str() Method:
1.Converting data types to strings:
  It converts any data type (e.g., integer, float, boolean) into its string representation. 
  This is useful when you need to concatenate different data types or display them to the user.
2.Creating custom string representations of objects:
  When you define a class in Python, you can implement the __str__() method to specify how objects of that class 
  should be represented as strings. This makes it easier to print or log objects in a readable format.