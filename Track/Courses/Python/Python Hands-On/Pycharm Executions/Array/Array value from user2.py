from array import *
arr=array('i',[])
n=int(input("Enter the length of the string"))
for i in range(n):
    x=int(input("Enter the value"))
    arr.append(x)
print(arr)
value=int(input("Enter the value for search"))
k=0
for e in arr:
    if e==value:
        print(k)
        break
    k=k+1
print(arr.index(value))