
#A string is a sequence

myName = "George"

nameLength = len(myName)

print nameLength

index = 0
for c in myName:
    print c, index
    index = index + 1
    
print "*******************"
print " "
print myName[1]


#Slice sequence
print myName[0] # This is the one at the begining
print myName[len(myName)-1] #This is the element at the end of the list
print myName[3:5] # This is the 4th element and the 5th element but not 6
print myName[3:] # From the 4th element to the end
print myName[:3] # From the start to the 4th element (not inclusive)
print myName[-3:] #Give you the last three elements

myName[4] = "T"  #This causes and error because strings are immuntable


