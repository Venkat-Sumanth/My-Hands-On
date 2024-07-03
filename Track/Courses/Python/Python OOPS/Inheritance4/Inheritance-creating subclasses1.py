class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@email.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

dev1 = Developer('venkata','sumanth',50000,'Python')
dev2=Developer('venu','suma',1600,'Java')

print(dev1.email)
print(dev1.prog_lang)

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

output:
venkata.sumanth@email.com
Python
50000
55000
