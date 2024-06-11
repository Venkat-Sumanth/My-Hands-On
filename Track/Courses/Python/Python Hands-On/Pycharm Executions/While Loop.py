i=1                   #initialization
while i<=5:           #condition
    print("Hello")    #increment(+)/decrement(-)
    i=i+1
#output:
Hello
Hello
Hello
Hello
Hello
----------------------------------------------------------------------------------------------
i=5
while i>=1:
    print("Boom ",i)
    i=i-1
#output:
Boom  5
Boom  4
Boom  3
Boom  2
Boom  1
----------------------------------------------------------------------------------------------
i=1
while i<=5:
    print("Telusko ",end="")
    j=1
    while j<=4:
         print("Rocks ",end="")
         j=j+1
    i=i+1
    print()
#output:
Telusko Rocks Rocks Rocks Rocks 
Telusko Rocks Rocks Rocks Rocks 
Telusko Rocks Rocks Rocks Rocks 
Telusko Rocks Rocks Rocks Rocks 
Telusko Rocks Rocks Rocks Rocks 
--------------------------------------------------------------------------------------------------
#Q)write a code to print all the values from 1 to 100 skip the numbers which are divisible by 3 or 5 
i=1
while i<=100:
    if i%3!=0 and i%5!=0:
        print (i)
    i=i+1
#output:
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
------------------------------------------------------------------------------------------------------
#write a code to print all the values from 1 to 100 skip the numbers which are not divisible by 3 or 5 
i = 1
while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
    i += 1
#output:
3
5
6
9
10
12
15
18
20
21
24
25
27
30
33
35
36
39
40
42
45
48
50
51
54
55
57
60
63
65
66
69
70
72
75
78
80
81
84
85
87
90
93
95
96
99
100
-----------------------------------------------------------------------------------------------------
Q)# # # #
  # # # #
  # # # #
  # # # #
i=1
while i<=4:
    j=1
    while j<=4:
       print("# ",end="")
       j=j+1
    print()
    i=i+1
output:
# # # #
# # # #
# # # #
# # # #
-------------------------------------------------------------------------------------------------------------

