import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

#I could have more functions in here...

if __name__ == "__main__":
    print distance(5,6,7,10)
