class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def shiftx(self, shift):
        self.x = self.x + shift

    def translate(self, xshift,yshift):
        self.x = self.x + xshift
        self.y = self.y + yshift

mypoint = Point()

print mypoint.x

mypoint.shiftx(10)

print mypoint.x

mypoint.shiftx(10)

print mypoint.x

print mypoint
