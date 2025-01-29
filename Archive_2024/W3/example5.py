

#open a file
f = open("points.txt", "r")

line = f.readline()

while line:
    print(line)
    line = f.readline()

f.close()
