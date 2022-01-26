
# Gathering inputs and constants
base = float(input("Enter the Base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

squareside = float(input('Enter the side of the square: '))

# Body of our program (Code)
# math, conditional statments, logic etc.

triangleArea = (base * height) * 0.5
#triangleArea = base * height / 2

squareArea = squareside**2 # The area of a square


# Present or Report on the results (output)

print("The area of that triangle is:",triangleArea)

print(squareArea == triangleArea)
