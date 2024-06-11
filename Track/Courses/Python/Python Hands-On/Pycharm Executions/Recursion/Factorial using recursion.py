def fact(n):
    if n==0:
        return 1        #once it returns the values to the code then it stops the functioning.
    return n*fact(n-1)  #Here n*fact(n-1), n=4,(n-1)-> 4-1=3, 3-1=2, 2-1=1, 1-1=0,0!=1
result = fact(4)
print(result)

output:
24
---------------------------------------------------------------------------------------------------------------------
- Recursion is a function calling itself.
1. Create a variable to store the factorial of a number.
2. Assign the variable by the fact() function and pass a number in it as an argument.
3. Print the value of the variable to get the result.
4. Define the function say fact() above the main code.
- A function can be defined by using the keyword def.
 def fact(n):
5. Call the same function inside the fact() function by applying the correct logic and return its value.
 return n*fact(n-1)
6. Apply the condition for the factorial of a 0 as it is always 1.
- In this way, the factorial of a number will be printed by using the recursion.