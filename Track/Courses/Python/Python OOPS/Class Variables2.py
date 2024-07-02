class Employee:

    num_of_emp=0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

        Employee.num_of_emp+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def appy_raise(self):
        self.pay = int(self.pay*self.raise_amount)

print(Employee.num_of_emp)

emp1=Employee('venkata','sumanth',50000)
emp2=Employee('venu','suma',1600)

print(Employee.num_of_emp)

print(emp1.pay)
emp1.appy_raise()
print(emp1.pay)

emp1.raise_amount = 1.05

print(emp1.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

output:
0
2
50000
52000
{'first': 'venkata', 'last': 'sumanth', 'pay': 52000, 'email': 'venkata.sumanth@company.com', 'raise_amount': 1.05}
1.04
1.05
1.04
