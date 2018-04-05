#Lecture
##Week 11 - More Working with Raster Data
#### Raster GIS Data Processing using Python and Numpy
###### Today we will continue our discussion on how to use arcpy to manipulate raster data.  We will explore toolboxes and manipulate data at the cell level (numpy)


1. arcpy.sa
  1. You can run almost every function in python
  2. WATCH OUT: arcpy.env extent and cell size ussually need to be set or results won't be right (Also watch out for No Data)
  3. eval function (for putting together large functions)
  4. save function (for saving output results)
  5. Raster function (for turning text paths into rasters)
  6. arcpy.RasterToNumPyArray and arcpy.NumPyArrayToRaster
  7. These functions are are used like cursors in vector data.
1. Numpy (http://www.numpy.org/)
  1. What is an array?
  2. Pay particular attendtion to cell size and extent, because numpy does NOT
  3. There are however a few functions that are more "GIS-y" that would be very hard to replicate in numpy and therefore GDAL has tools for these operations.
    1. Raster to vector conversion and back
    2. Raster Proximity functions

  

#Lab 

Here is your assignment (You have two weeks to finish this assignment).

Download the data in this weeks folder.

1. Write a script that does the following:
  1. Uses numpy to rewite the script from last week (except Euecldian distance) so that it runs using numpy instead of spatial analysis tools.








  




      
      

