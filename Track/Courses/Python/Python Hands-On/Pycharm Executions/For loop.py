x=["sumanth",65,2.5]
for i in x:
    print(i)
output:
sumanth
65
2.5
-----------------------------------------------------------------------------------------------------------------
x="sumanth"
for i in x:
    print(i)
output:
s
u
m
a
n
t
h
------------------------------------------------------------------------------------------------------------------
for i in [2,6,'suma']:
    print(i)
output:
2
6
suma
--------------------------------------------------------------------------------------------------------------
for i in range(10):
    print(i)
output:
0
1
2
3
4
5
6
7
8
9
-------------------------------------------------------------------------------------------------------------
for i in range(11,21,2):
    print(i)
output:
11
13
15
17
19
-------------------------------------------------------------------------------------------------------------------
for i in range(20,10,-2):
    print(i)
output:
20
18
16
14
12
------------------------------------------------------------------------------------------------------------------
for i in range(1,21):
    if i%5!=0:
        print(i)
output:
1
2
3
4
6
7
8
9
11
12
13
14
16
17
18
19
---------------------------------------------------------------------------------------------------------------------
In Python, break, continue, and pass are control flow statements that are used to
alter the normal flow of execution in a loop or conditional statement.

#1
break: The break statement is used to terminate a loop prematurely when a certain condition is met. 
Once the break statement is encountered inside a loop, the loop is immediately terminated and the program continues 
with the next statement after the loop.
for i in range(1, 6):
    if i == 3:
        break
    print(i)
output:
1
2

#2
continue: The continue statement is used to skip the current iteration of a loop and move on to the next iteration, 
without executing the remaining code in the loop for the current iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
output:
1
2
4
5

#3
pass: The pass statement is a placeholder statement that is used to indicate that no action should be taken. 
It is often used as a placeholder when writing code that will be filled in later.
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)
output:
1
2
4
5