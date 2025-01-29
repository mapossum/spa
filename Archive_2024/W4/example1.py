myname = "George" #String

#Strings are sequences <--todays topic

#This loop goes through each element in a sequence
for char in myname:
    print(char)

print(len(myname))

#This loop is functionally equivalent to the previous one.
#But it uses a while loop and increments and index
index = 0
while index < len(myname):
    print(myname[index])
    index += 1

part = myname[2:-2]
print(part)
