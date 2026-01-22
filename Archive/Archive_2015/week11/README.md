#Lecture
##Week 11 - Working with Raster Data in GDAL / Open Source
#### Raster GIS Data Processing using Python using GDAL and Numpy
###### Today we will discuss how to use manipulate raster data in GDAL and Numpy


1. numpy can be used for many local operations, conditional operators, finding global min, global max etc.  You can even use it for zonal functions.
  1. Pay particular attendtion to cell size and extent, because numpy does NOT
2. There are however a few functions that are more "GIS-y" that would be very hard to replicate in numpy and therefore GDAL has tools for these operations.
  1. Raster to vector conversion and back
  2. Raster Proximity functions
3. Python GDAL "Cookbook": http://pcjericks.github.io/py-gdalogr-cookbook/
  

#Lab 

Here is your assignment (You have two weeks to finish this assignment).

The assignment for this week, is the same as for last week, only this week you will not use arcpy, only GDAL with python.

1. Write a simple script that finds the mean of all either all the precip or temp rasters (GDAL does not read geodatabases, only image formats, so you will have to convert them manually or using arcpy).
2. Write a script that does the following:
  1. Take each of the shapefiles that start with "Risk_"
  2. Use Euclidian distance to create a raster of straight line distance from each of these datasets (in GDAL this is called Proximity, but proximity only takes rasters, so you have to do a vector to raster conversion first).
  3. Adjust the output so that only distances to 1000m are present (no data beyond 1000m)  (You can use numpy for this step and the next, using the where function).
  4. Reverse the values in the each of these datasets so the values start at 1000 and end at 0 in places that are 1000m away from the feature.
  5. add up each of these datasets and save the output (again use numpy).







  




      
      

