

#open a file
f = open("points.txt", "r")

#read the contents of the file
fcontents = f.read()

print(fcontents)
print(type(fcontents))

f.close()
