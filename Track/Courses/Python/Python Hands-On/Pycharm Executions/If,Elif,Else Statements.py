#If Statement:
if True:
    print('i am right')
-------------------------------------------------------------------------------------------------------------
#If_Else Statement:
x=6
r=x%2
if r==0:
    print('Even')
else:
    print('Odd')
--------------------------------------------------------------------------------------------------------------
#Nested If Statement:
x=70
r=x%2
if r==0:
    print('Even')
    if x>5:
        print('Great')
    else:
        print('Not So Great')
else:
    print('odd')
---------------------------------------------------------------------------------------------------------------
#Elif Statement:
x=6
if x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")
elif x==4:
    print("four")
else:
    print("wrong input")
--------------------------------------------------------------------------------------------------------------
- CPU has three parts: CU (Control Unit), ALU ( Arithmetic Logic Unit) and MU ( Memory unit).
- MU is used to store variables and data.
- ALU has two parts:
1. AU - Arithmetic Unit ( it performs mathematical calculations)
2. LU - Logical Unit ( it makes a computer think something)

Syntax:-
 if (condition):
  statement;
  
Indentation:-
- In Python, we have to follow certain indentations that specify the conditions that are present 
  inside a certain block.
- Indentation simply means a certain number of spaces at the beginning of a code line.
- Indentation increases the readability of the code.

Nested if and else statements:-
- Nested if and else statements are also allowed in Python. 
- if statement can also be checked inside other if statement. This conditional statement 
  is called a nested if statement.
- In nested, the inner if condition will be checked only if the outer if condition is 
  true and that helps to see multiple conditions to be satisfied.
- Round brackets for putting a condition in the if statement is optional. 

if, elif and else statements:-
- elif stands for if-else.
- The if-elif statement is a shortcut of if..else chain.
- If the if condition s false, then the condition inside the elif will be checked and executed.
- While using if-elif statement at the end else block is added that will be executed when none of the above 
  if-elif statements is true.

