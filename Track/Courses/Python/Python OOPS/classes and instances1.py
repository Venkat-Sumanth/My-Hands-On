class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('suma','venkat',50000)
emp_2 = Employee('rani','paradise',60000)

emp_1.first = 'suma'
emp_1.last = ' venkat'
emp_1.email = 'suma.venkat@company.com'
emp_1.pay = 50000

emp_2.first = 'rani'
emp_2.last = ' paradise'
emp_2.email = 'rani.paradise@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

output:
suma.venkat@company.com
rani.paradise@company.com
suma  venkat
rani  paradise
