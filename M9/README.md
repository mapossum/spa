#Lecture
##Week 9 - More Working with Raster Data
#### Raster GIS Data Processing using Python and Numpy
###### Today we will continue our discussion on how to use arcpy to manipulate raster data.  We will explore toolboxes and manipulate data at the cell level (numpy)


1. arcpy.sa continued
  1. arcpy.RasterToNumPyArray and arcpy.NumPyArrayToRaster
  2. These functions are are used like cursors in vector data.
1. Numpy (http://www.numpy.org/)
  1. What is numpy?
  2. What is an array?
  3. Pay particular attendtion to cell size and extent, because numpy does NOT
  4. There are however a few functions that are more "GIS-y" that would be very hard to replicate in numpy and GDAL has tools for these operations but beyond scope of our course.
    1. Raster to vector conversion and back
    2. Raster Proximity functions

  

#Lab 

Here is your assignment.

Download the data in this weeks folder.  It is a temperature average for the entire year.  Simmilar to last week, you will add up all the temperature values using a loop and the eval statement.  This time use numpy.

1. Write a script that does the following:
  1. Uses numpy to rewite the script from last week (except Euecldian distance) so that it runs using numpy instead of spatial analysis tools. 


Videos:
1) https://youtu.be/-QeYpjPULok
2) https://youtu.be/I9cQYETIkG0
3) https://youtu.be/yrrNDVPGCSo







  




      
      

