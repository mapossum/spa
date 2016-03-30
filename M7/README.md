#Lecture
##Meeting 7 - Working with GIS data
####Today we review GIS Data structures and talk about how they can accessed programattically.

1.  What is GIS Data?
  1. Points, Lines, Polygons
    1. What is a Point?
    2. What is a Line?
    3. What is a Polygon?
  2. Table Data
  3. Linked together
  4. Raster Data (We will talk more about that in a couple weeks)
2. What can GIS systems do with GIS data?
  1. GIS operations. (Vary by library)
    1. Examples
      1. Union
      2. Interset
      3. Buffer
      4. Difference
3. Implmenting in Arcpy
  1. The data access module (da) - http://resources.arcgis.com/en/help/main/10.1/index.html#/What_is_the_data_access_module/018w00000008000000/
  2. Cursors
    1. Search
    2. Insert
    3. Update
  3. Working with Geometries
    1. Creating Points, Lines, Polygons

#Lab 

Here is your assignment

Write a python program that does the following:
Take a point shapefile that has contains two fields.  In our case one will be called "Animal" and one field called "Time".  
The Point shapefile represents animal movements acquired using a GPS collar.  
1) You must create a line shapefile that contains one line per animal representing the movements of that animal from the earliest time to the latest time.
2) Your program should also create a polygon shapefile that represents the animal’s home range.  The home range will be defined as the polyline shapefile you create buffered by 0.1 km.
3) Your program should also find the amount of each animal's home range that is within each feature of another dataset called "Parks". (Find the amount of each home range that is within a park (Think GIS Intersect)).

Use the accompanying point GIS shapefile to test your program.

Video: https://www.youtube.com/watch?v=UMyzk9mzY68



  




      
      

