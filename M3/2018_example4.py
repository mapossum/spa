
#A string is a sequence

myName = "George"


def countChar(testString,e):
    # "Number of times e appeared
    t = 0
    for letter in testString:
        if letter.upper() == e:
            t = t + 1
    return t

testText = "The University of Southern Mississippi is one of only 76 public universities to earn the Carnegie "
testChar = "U"

print countChar(testText, testChar)


    


