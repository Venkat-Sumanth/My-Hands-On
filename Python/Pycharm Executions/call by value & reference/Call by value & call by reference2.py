https://www.youtube.com/watch?v=fnGR0bVtK6g

Call by value:
def change(x):      # x is formal parameter
    x=x+10
    print(x)
a=10                # a is actual parameter
print(a)
change(a)
print(a)

output:
10
20
10
---------------------------------------------------------------------------------------------------------------------
string = "welcome"
List = [10,20,5,30]
print(string)
print(List)
List[1] = List[1]+20
print(List)
string[1] = "R"        #if we ignore this line we get below output

output:
welcome
[10, 20, 5, 30]
[10, 40, 5, 30]
----------------------------------------------------------------------------------------------------------------------
Call by Reference:
def change(x):         #Here x is list
    x[1]=x[1]+20
    print(x)
    print(id(x))
a=[10,20,30,40]
print(a)
change(a)
print(a)
print(id(a))

output:
[10, 20, 30, 40]
[10, 40, 30, 40]
2504149029120
[10, 40, 30, 40]
2504149029120
--------------------------------------------------------------------------------------------------------------------