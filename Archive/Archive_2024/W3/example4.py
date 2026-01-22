

#open a file
f = open("points.txt", "r")

linenumber = 1
for line in f:
    print("Line number {} says: ".format(linenumber))
    print(line)
    linenumber = linenumber + 1

f.close()
