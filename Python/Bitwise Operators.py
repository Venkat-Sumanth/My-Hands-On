                                            Bitwise Operator
--------------------------------------------------------------------------------------------------------------
1)Complement Operator:
>>> ~12
-13
>>> ~45
-46
>>> ~121
-122
-------------------------------------------------------------------------------------------------------------
2)AND Operator:
>>> 12&13
12
>>> 25&30
24
--------------------------------------------------------------------------------------------------------------
3)OR Operator:
>>> 12|13
13
---------------------------------------------------------------------------------------------------------------
4)XOR(^) Operator:
>>> 12^13
1
>>> 25^30
7
-------------------------------------------------------------------------------------------------------------
5)Left Shift Operator:
>>> 10<<2
40
>>> a=20
>>> a<<2
80
--------------------------------------------------------------------------------------------------------------
6)Right shift Operator:
>>> 20>>2
5
------------------------------------------------------------------------------------------------------------
- In bitwise operations, the integers are first converted into binary and then operations are performed by bitwise operators on each bit or corresponding pair of bits.
- The result is returned in decimal format by the bitwise operators.
- There are six types of binary operators:-
1. Complement (~)
2. And (&)
3. Or (|)
4. XOR (^)
5. Left Shift 
6. Right Shift 

- Complement operator is also known as tilde(~) operator.
- Complement simply do the reverse of binary form. If a bit is 0 then it makes it 1 and vice-versa.
- Reverse of each bit of a number returns the 1's complement.
- We can store only positive numbers in our system and that's why we find the 2's complement 
  of each negative number.
 2's complement = 1's complement +1

-AND operator will return true if both the conditions are true while the OR operator will 
 return true if at least one condition is true.
 
 - XOR operator will return 1 or true when there is an odd number of 1 bit present in operations and if there is an even number of 1, 
   then it will return 0.
   
  - Leftshift operator shift bits on the left-hand side. The right-shift operator shifts 
    bits on the right-hand side.
-   Leftshift add the bits while the right-side removes the bits.