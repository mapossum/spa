import math

myname = "George Raber"

print len(myname)  # Gets the length of the sequence

print myname[0] # Gets the first item in the sequence

print myname[3]  # Gets the fourth item in the sequence

print myname[0:6] #Gives us a slice of the sequence

print myname[3:] #Gives us a slice of the sequence from 3 to the end
print myname[:8] #Gives us a slice of the sequence from begining to 8

print myname[1:-1] #You can use negative numbers in slices

print "F" in myname

print myname.upper()
print myname.replace("George", "Georgia")

def getLastname(inputName):
    spindex = inputName.find(" ") + 1
    return inputName[spindex:]

print getLastname(myname)

names = myname.split(" ")

print names
print type(names)

print names[0]  # print first element of the list (names)
print names[1]  # print second element of the list (names)

print myname.split(" ")[1]  #returns last name (second item in list which was created by the split)


