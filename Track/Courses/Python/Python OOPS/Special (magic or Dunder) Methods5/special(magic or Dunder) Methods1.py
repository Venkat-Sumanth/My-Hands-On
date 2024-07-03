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

emp1=Employee('venkata','sumanth',50000)
emp2=Employee('venu','suma',1600)

print(emp1)
print(repr(emp1))
print(str(emp1))

output:
venkata sumanth - venkata.sumanth@email.com
Employee('venkata', 'sumanth', '50000')
venkata sumanth - venkata.sumanth@email.com

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