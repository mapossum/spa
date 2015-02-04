

f = open(r"C:\courses\spa\week4\cities.txt", "r")
f2 = open(r"C:\courses\spa\week4\citiesSubset.txt", "w")

count = 1
for line in f:
    print line.strip()
    count += 1
    if (count % 100) == 0:
        f2.write(line)

f.close()
f2.close()

#special char for new line

print "\n"


f = open(r"C:\courses\spa\week4\citiesthing.txt", "r")





