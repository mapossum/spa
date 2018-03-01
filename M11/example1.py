import arcpy
import numpy

arcpy.env.overwriteOutput = True
# Create a simple array from scratch using random values
myArray = numpy.random.random_integers(0,100,25) #numpy.ones(25) * 5 #
myArray.shape = (5,5)
print myArray

# Convert array to a geodatabase raster
point = arcpy.Point(50, 50)
myRaster = arcpy.NumPyArrayToRaster(myArray,lower_left_corner=point,x_cell_size=10)
myRaster.save("C:/temp/myRandomRaster4.tif")
