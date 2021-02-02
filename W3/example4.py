

#open a file
f = open("points.txt", "r")

for line in f:
    print(line)

f.close()
