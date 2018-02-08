

def bardata(s):
    ltdict = {}

    for c in s:
        ctest = c.upper()
        if not ctest in ltdict:
            ltdict[ctest] = 0
        ltdict[ctest] +=1

    return ltdict

gettys = "But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."

output = bardata(gettys)

k = list(output.keys())

k.sort()

for key in k:
    print key, output[key]


const = "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."

output = bardata(const)

k = list(output.keys())

k.sort()

for key in k:
    print key, output[key]
    


