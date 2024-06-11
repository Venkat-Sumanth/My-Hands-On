nums = [7,8,9,5]
print(nums[1])

output:
8
---------------------------------------------------------------------------------------------------------------
nums = [7,8,9,5]
for i in nums:
    print(i)
    
output:
7
8
9
5
---------------------------------------------------------------------------------------------------------------
nums = [7,8,9,5]
it=iter(nums) #iter() function converts list into iterator #iterator will give only one value at a time
print(it)

output:
<list_iterator object at 0x0000014C60C66F20>
#it prints the object of iterator
---------------------------------------------------------------------------------------------------------------
nums = [7,8,9,5]
it=iter(nums) #iter() function converts list into iterator #iterator will give only one value at a time
print(it.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()

output:
7
---------------------------------------------------------------------------------------------------------------
nums = [7,8,9,5]
it=iter(nums)  #iter() function converts list into iterator #iterator will give only one value at a time
print(it.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()
print(it.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()

output:
7
8
---------------------------------------------------------------------------------------------------------------
nums = [7,8,9,5]
it=iter(nums)  #iter() function converts list into iterator #iterator will give only one value at a time
print(it.__next__()) #it prints the first value in a list, instead of using index value we can use .__next__()
print(next(it))  #it prints the next value in a list
for i in nums:
    print(i)
    
output:
7
8
7
8
9
5
---------------------------------------------------------------------------------------------------------------
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):  #This __iter__() method will give the object of iterator
        return self
    def __next__(self):  #This __next__() gives the next value
        if self.num<=10:
            val=self.num #val is variable 
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen() #values is object and TopTen is constructor class
for i in values:
    print(i)
    
output:
1
2
3
4
5
6
7
8
9
10
---------------------------------------------------------------------------------------------------------------
