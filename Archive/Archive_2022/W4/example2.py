myname = ("George", "Thomas", "Raber")

#This loop goes through each element in a sequence
for name in myname:
    print(name)

print(len(myname))

#This loop is functionally equivalent to the previous one.
#But it uses a while loop and increments and index
index = 0
while index < len(myname):
    print(myname[index])
    index += 1
