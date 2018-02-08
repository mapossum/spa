
def readFileToList(path, hasHeader=True):
    f = open(path, "r")

    fileLines = []

    for line in f.readlines():
        fileLines.append(line.strip())

    f.close()

    if hasHeader:
        fileLines = fileLines[1:]

    return fileLines

fileData = readFileToList(r"C:\temp\spa\M4\citiesSmall.txt")

print fileData


