

def is_triangle(a,b,c):

    test1 = (a + b) > c
    test2 = (c + b) > a
    test3 = (a + c) > b

    return test1 and test2 and test3

side1 = raw_input("Enter Side 1:")
side2 = raw_input("Enter Side 2:")
side3 = raw_input("Enter Side 3:")


print is_triangle(float(side1),float(side2),float(side2))
