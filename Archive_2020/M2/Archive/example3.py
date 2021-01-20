

def countLetters(testString,testChar):
    count = 0

    for char in testString:
        if (char.upper() == testChar.upper()):
            count = count + 1

    return count


name1 = raw_input("What is the name? ")

while(name1 <> "STOP"):
    print name1

    c = countLetters(name1,"E")

    print 'The count of "E" is ' + str(c)

    name1 = raw_input("What is the name? ")
