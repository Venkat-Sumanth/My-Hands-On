def count(list):  #Here count() is function and list is argument/parameter in it.
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1 #This line increments the variable even by 1. It indicates that the current number i is even, so the count of even numbers is increased.
        else:
            odd+=1 #This line increments the variable odd by 1. Since the condition for even numbers wasn't met, this line indicates that the current number i is odd, and the count of odd numbers is increased
    return even,odd
list=[20,15,14,19,16,24,28,47,26]
even,odd=count(list)  #It calls the count function with the list argument (assumed to be a list of numbers).
print(even)
print(odd)

output:
6
3
--------------------------------------------------------------------------------------------------------------------
def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
list=[20,15,14,19,16,24,28,47,26]
even,odd=count(list)
print("Even :{} and odd :{}".format(even,odd)) #.format() is a function belongs to string.

output:
Even :6 and odd :3