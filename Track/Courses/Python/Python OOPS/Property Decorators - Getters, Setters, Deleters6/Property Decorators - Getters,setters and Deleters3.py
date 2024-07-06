class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
    @property      #property decorator is used to make email as attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property    #property decorator is used to make fullname as attribute
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self, name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Delete Name! ')
        self.first = None
        self.last = None

emp1 = Employee('venkata','sumanth')

emp1.fullname = 'subhash chandra'  #after writing the @fullname setter, emp1 fullname works

# emp1.first = 'Jim'  #we modified first name 'venkata' to 'Jim'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname

output:
subhash
subhash.chandra@email.com
subhash chandra
Delete Name! 

getter — it is used to access the value of the attribute.
setter — it is used to set the value of the attribute.
deleter — it is used to delete the instance attribute.

