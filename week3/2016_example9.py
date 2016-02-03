mylist = range(1,200)


#for i in range(1,201):
#    print i, i % 7

ages = [40,38,36]
weight = [215,120,165]
names = ["George", "April", "Lloyd"]

people = zip(names,ages,weight)
print people

print "Name, Age"
for person in people:
    print person[0], ",", person[1]







