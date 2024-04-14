Break:
available = 6
x=int(input("How many candies you want?"))
i=1
while i<=x:
    if i>available:
        print("out of stock")
        break
    print("candy")
    i=i+1
print("Bye")
output:
How many candies you want?7
candy
candy
candy
candy
candy
candy
out of stock
Bye
------------------------------------------------------------------------------------------------------------------
Continue:
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)
print("bye")
output:
1
2
4
7
8
11
13
14
16
17
19
22
23
26
28
29
31
32
34
37
38
41
43
44
46
47
49
52
53
56
58
59
61
62
64
67
68
71
73
74
76
77
79
82
83
86
88
89
91
92
94
97
98
bye
----------------------------------------------------------------------------------------------------------------------
Pass:
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)
output:
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
-------------------------------------------------------------------------------------------------------------------
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