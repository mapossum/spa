

name1 = raw_input("What is the name? ")

while(name1 <> "STOP"):
    print name1

    count = 0

    for char in name1:
        if ((char == "E") or (char == "e")):
            count = count + 1

    print count

    name1 = raw_input("What is the name? ")
