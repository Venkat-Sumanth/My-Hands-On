#Continue:
for i in range(5):
    if i==3:
        continue
    print("Hello ",i)
output:
Hello  0
Hello  1
Hello  2
Hello  4
--------------------------------------------------------------------------------------------------------------------
#Break:
for i in range(5):
    if i==3:
        break
    print("Hello ",i)
output:
Hello  0
Hello  1
Hello  2
