
f = open(r'C:\courses\spa\week4\citiesSmall.txt', 'r')

for line in f:
    print line.strip().split(",")[0]
