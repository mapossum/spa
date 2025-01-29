

a = 3
b = 0

#Examples of simple conditional statements
if a > b:
    print("A is greater than B")

if a == b:
    print("A is equal to B")

if a < b:
    print("A is less than B")

if a >= b:
    print("A is greater than or equal to B")

if a != b:
    print("A is not equal to B")

if a:
    print("A is not zero")


#Examples of Logical Operators joining multiple conditional statements

if (a > b) and (a < 5):
    print("a is between b and 5")

if (a < b) and (a > 5):
    print("a is between 5 and b")

if (a < b) and (a < 5):
    print("a is less than both b and 5")

if not a:
    print("A is zero")


#Examples of nesting conditionals
if (a > b):
    print("a is less than b")
    if (a < 5):
        print("a is between b and 5")

#Examples of an else statement

if (a > b):
    print("a is greater than b")
else:
    print("a is less than or equal to b")


if (a > b):
    print("a is greater than b")
elif(a == b):
    print("a equal to b")
else:
    print("a is less than b")
        

