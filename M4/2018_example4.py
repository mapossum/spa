
f = open(r"C:\temp\spa\M4\citiesSmall.txt", "r")

for line in f.readlines():
    print line.strip().split(",")

f.close()



