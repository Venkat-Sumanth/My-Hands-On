def topten():  #we converted this function into generator through yield keyword
    yield 5   #yield is keyword which will make function as generator, like return yield also will give value
values=topten() #we are calling the function
print(values)

output:
<generator object topten at 0x0000026555D04930>
#It returns the generator object
----------------------------------------------------------------------------------------------------------------
def topten():   #we converted this function into generator through yield keyword
    yield 1
    yield 2
    yield 3
    yield 4
values=topten()  #we are calling the function
print(values.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()

output:
1
#yield is keyword which will make function as generator, like return yield also will give value
#In yield, since its a generator which will give us iterator we can write multiple yield statements
---------------------------------------------------------------------------------------------------------------
def topten():   #we converted this function into generator through yield keyword
    yield 1
    yield 2
    yield 3
    yield 4
values=topten()      #we are calling the function
print(values.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()
print(values.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()

output:
1
#yield is keyword which will make function as generator, like return yield also will give value
#In yield, since its a generator which will give us iterator we can write multiple yield statements
---------------------------------------------------------------------------------------------------------------
def topten():   #we converted this function into generator through yield keyword
    yield 1
    yield 2
    yield 3
    yield 4
values=topten()   #we are calling the function
print(values.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()
print(values.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()
for i in values:
    print(i)

output:
1
2
3
4
#yield is keyword which will make function as generator, like return yield also will give value
#In yield, since its a generator which will give us iterator we can write multiple yield statements
---------------------------------------------------------------------------------------------------------------
Example problem : Print first 10 perfect square Numbers

def topten():   #we converted this function into generator through yield keyword
    n=1
    while n<=10:
        sq=n*n
        yield sq  #yield is keyword which will make function as generator, like return yield also will give value
        n+=1
values = topten()   #we are calling the function
for i in values:
    print(i)
    
output:
1
4
9
16
25
36
49
64
81
100
#yield is keyword which will make function as generator, like return yield also will give value
#In yield, since its a generator which will give us iterator we can write multiple yield statements
--------------------------------------------------------------------------------------------------------
why do we use generators?
Assume that we are fetching 1000 records from a database, to process something with those records, 
we can work with one record/one value at a time.so, that's why we use generators

-Difference between yield and return is return will terminate the function, 
yield will not terminate the function

