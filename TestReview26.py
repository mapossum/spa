def div(a,b):
    if b == 0:
        return -1
    else:
        return a/b

def dividethat(x,y):
    outSeq = []
    for v in y:
        outSeq.append(div(x,v))
    return outSeq

a = [4,7,2,5,0,7,2,6]

print(dividethat(3,a))
