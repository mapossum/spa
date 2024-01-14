myname = "George"

#This loop goes through each element in a sequence
for letter in myname:
    print(letter)

print(len(myname))

#This loop is functionally equivalent to the previous one.
#But it uses a while loop and increments and index
index = 0
while index < len(myname):
    print(myname[index])
    index += 1
