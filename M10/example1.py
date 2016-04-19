import arcpy
import numpy

# Create a simple array from scratch using random values
myArray = numpy.random.random_integers(0,100,2500)
myArray.shape = (50,50)

# Convert array to a geodatabase raster
point = arcpy.Point(100, 100)
myRaster = arcpy.NumPyArrayToRaster(myArray,lower_left_corner=point,x_cell_size=1)
myRaster.save("C:/temp/myRandomRaster1.tif")
