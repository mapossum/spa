

#open a file
f = open("points.txt", "r")

for line in f:
    ls = line.split()
    x = float(ls[0])
    y = float(ls[1])
    print(x,y)

f.close()
