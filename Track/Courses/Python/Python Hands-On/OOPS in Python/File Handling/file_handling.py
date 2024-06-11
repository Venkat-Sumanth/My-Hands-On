s=open('demo',mode='r') #s is holding variable, demo is file name and r is read mode
print(s.read()) #read() mode going on
s.close() #we are closing the file after mode performed

output:
My name is venkat sumanth Bethanapalli
I am from visakhapatnam
I studied at KL Uiversity
I am innocent boy but i m a matured boy
I am trying to write code in a next

#r - read: we can read the file
--------------------------------------------------------------------------------------------------
s=open('demo',mode='w') #s is holding variable, demo is file name and w(truncate) is write mode
s.write('bye bye') #we are passing write statement to execute
s.close() #we are closing the file after mode performed

output:
bye bye

#w - write(Truncate): we write the file, if the old data is there then it will be erased 
 and newly written data will be added
--------------------------------------------------------------------------------------------------
s=open('demo',mode='a') #s is holding variable, demo is file name and a is append mode
s.write(' jagan') #Hence its a append mode the data in write statement adds at the end
s.close() #we are closing the file after mode performed

output:
bye bye jagan

#a - append: data will be added at the last/end
--------------------------------------------------------------------------------------------------
s=open('demo','r+') #s is holding variable, demo is file name and r+ is read and write mode
print(s.read())
s.write(' suman')
s.close() #we are closing the file after mode performed

output:
bye bye jagan suman

#r+ - read write: we can read and write the file simultaneouslye 
--------------------------------------------------------------------------------------------------
s=open('demo',mode = 'w+') #s is holding variable, demo is file name and w+(truncate) is write and read mode
s.write('sumanth is very good boy')
print(s.read())
s.close() #we are closing the file after mode performed

output:
sumanth is very good boy

#w+ - write read(Truncate): w+ mode it allows us to read and write data in the file. 
 If the file does not exist, w+ mode creates a new file and opens it.
---------------------------------------------------------------------------------------------------
-while we pass the parameters we need to define two here. 
 (i)File name (ii)mode/purpose of file means reading, overwriting, writing etc.

File Handling:
Reading, writing, deleting, creating of a file is called file handling

Execution the way we do:
open -> open()  #we open the file
Read/write/delete/create  #we do operation
close -> close() #we close the file

Mode/operation/purpose:
r - read #we can read the file
w - write(Truncate) #we write the file, if the old data is there then it will be erased and newly written data will be added
a - append  #data will be added at the last/end
r+ - read write #we can read and write the file simultaneously
w+ - write read(Truncate) #w+ mode it allows us to read and write data in the file. If the file does not exist, w+ mode creates a new file and opens it.

-Why File?
-when we write a code we use variables and in those variables we will be storing some data.
 Now, most of the data we use in variables are temporary data .
 if we want to count variable, 
 if we want to store some data that we store in variable. 
 But what if we want to save a data for longer period.
 The moment we close our application we will lose all the data. 
 But, what the things is even if we close the application the data should be 
 stored somewhere and that's where we need to find permanent storage.
 what if we store something for a longer period but then in a simple format and 
 best way is to go for is text