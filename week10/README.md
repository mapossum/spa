#Lecture
##Week 9 - Working with Raster Data
#### Raster GIS Data Processing using Python
###### Today we will discuss how to use arcpy to manipulate raster data


1. Review of raster operations:
  1. Local
  2. Neighborhood
  3. Zonal and Global
2. Very useful functions
  1. Con (conditional statement) basically an if-then statement.
  2. Arithmetic operations
  3. Set Null (assigns a no data value to an area)
3. arcpy.sa
  1. You can run almost every function in python
  2. WATCH OUT: arcpy.env extent and cell size ussually need to be set or results won't be right (Also watch out for No Data)
  3. eval function (for putting together large functions)
  4. save function (for saving output results)
  5. Raster function (for turning text paths into rasters)
  6. arcpy.RasterToNumPyArray and arcpy.NumPyArrayToRaster (More on this next week)

  

#Lab 

Here is your assignment (You have two weeks to finish this assignment).

Download the data in this weeks folder.

1. Write a simple script that finds the mean of all either all the precip or temp rasters.
2. Write a script that does the following:
  1. Take each of the shapefiles that start with "Risk_"
  2. Use Euclidian distance to create a raster of straight line distance from each of these datasets.
  3. Adjust the output so that only distances to 1000m are present (no data beyond 1000m).
  4. Reverse the values in the each of these datasets so the values start at 1000 and end at 0 in places that are 1000m away from the feature.
  5. add up each of these datasets and save the output.







  




      
      

