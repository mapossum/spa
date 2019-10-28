#Lecture
##Week 8 - Working with Raster Data
#### Raster GIS Data Processing using Python
###### Today we will discuss how to use arcpy to manipulate raster data

2018 Lecture Video: https://youtu.be/bWkHGZOym-g

2018 Lab Video: https://youtu.be/eG8BbFnN-lc

1. Review of raster operations:
  1. Local
  2. Neighborhood
  3. Zonal and Global
2. Very useful functions
  1. Con (conditional statement) basically an if-then statement.
  2. Arithmetic operations
  3. IsNull (assigns a no data value to an area)
3. arcpy.sa
  1. You can run almost every function in python
  2. WATCH OUT: arcpy.env extent and cell size ussually need to be set or results won't be right (Also watch out for No Data)
  3. eval function (for putting together large functions)
  4. save function (for saving output results)
  5. Raster function (for turning text paths into rasters)
  6. http://desktop.arcgis.com/en/arcmap/10.5/extensions/spatial-analyst/map-algebra/working-with-raster-objects.htm
  7. arcpy.RasterToNumPyArray and arcpy.NumPyArrayToRaster (next week)

  

#Lab 

Here is your assignment (You have two weeks to finish this assignment).

Download the data in this weeks folder.

1. Write a script that does the following:
  1. Take each of the shapefiles that start with "Risk_"
  2. Use Euclidian distance to create a raster of straight line distance from each of these datasets.
  3. Subtract the values in the Euclidian output from 1000.
  4. Set all the negative values to 0.
  5. add up each of these datasets and save the output.
  
  
Old YouTube Link:  https://www.youtube.com/watch?v=e0V_mMspZc8

  








  




      
      

