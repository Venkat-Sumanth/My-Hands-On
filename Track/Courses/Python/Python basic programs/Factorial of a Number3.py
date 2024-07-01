def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=5
result=fact(n)
print(result)

output:
120
-----------------------------------------------------------------------------
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=5
result=fact(n)
print(result)

output:
120

