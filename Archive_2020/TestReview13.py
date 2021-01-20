def createRange1(x):
    outSeq = []
    for c in range(0,x):
        outSeq.append(c % 3 + 1)
    return outSeq

def createRange2(x):
    outSeq = []
    c = 0
    while x > c:
        outSeq.append(c % 3 + 1)
        print(c)
        c = c + 1  ##THIS IS THE LINE REFERENCED BELOW
    return outSeq

def multiplySeq(x,y):
    for i in range(0,len(x)):
        x[i] = x[i] * y[i]

myL1 = createRange1(9)
myL2 = createRange2(9)

multiplySeq(myL1,myL2)

