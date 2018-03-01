myd = { "George": 39, "April": 37, "Lloyd": 35 }

#Small cities Dictionary
Cites = {"Hattiesburg": {"Population" : 50000, "Area": 300}}


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

print histogram("The quick brown fox jumps over the lazy dog!")


