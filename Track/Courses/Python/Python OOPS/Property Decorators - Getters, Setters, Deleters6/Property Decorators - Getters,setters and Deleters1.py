class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first + '.' +last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1 = Employee('venkata','sumanth')

emp1.first = 'Jim'  #we modified first name 'venkata' to 'Jim'

print(emp1.first)
print(emp1.last)
print(emp1.fullname())

output:
Jim
sumanth
Jim sumanth

getter — it is used to access the value of the attribute.
setter — it is used to set the value of the attribute.
deleter — it is used to delete the instance attribute.