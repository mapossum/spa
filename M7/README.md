#Lecture
##Meeting 6 - Working with Vector GIS Data with Python II


1.  What is GIS Data? 
  1. Points, Lines, Polygons
    1. What is a Point?
    2. What is a Line?
    3. What is a Polygon?
  2. Table Data
  3. Linked together
  4. Raster Data (We will talk more about that in a couple weeks)
2. Implmenting in Arcpy
  1. The data access module (da)
  2. Cursors
    1. Search - Accessing Data Only (reading)
    2. Insert - Creating new data (adding records)
    3. Update - Changing record values - simmilar to Calculate Field Tool, but more powerful.
  3. Converting Vector Data from / to Numpy arrays.
    1. Scipy & Numpy
      1. What is an array?  https://docs.scipy.org/doc/numpy/index.html
      2. Array functions and utilites.
        1. Create Arrays: https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html
        2. Array Functions: https://docs.scipy.org/doc/numpy/reference/index.html
    2. FeatureClassToNumPyArray and TableToNumPyArray
    3. NumPyArrayToTable and NumPyArrayToFeatureClass
    4. ExtendTable
  4. Reading Geometries - https://pro.arcgis.com/en/pro-app/arcpy/get-started/reading-geometries.htm
  5. Writing Geometries - https://pro.arcgis.com/en/pro-app/arcpy/get-started/writing-geometries.htm
  
	
Videos:<br>
https://youtu.be/3j_fSkT4FQA and <br>
https://youtu.be/UjHiBCBhCEY

#Lab 

Here is your assignment.

1) We are goingt to start the assignment together in class.  I have included a file called turtleData.py.  It reads information off a turtle tracking website.  I will explain the data that comes from the site that we can read into a python list.  Each element represents a single turtle location.  First you will notice that by changing the URL accessed you can get the data for a different turtle.  There are a total of 244 turtles (Ids of 1-244).  You will create a polyline shapefile and then read each turtle data in and construct a polyline feature for that turtle.  To get full credit include a TurtleID field in the output shapefile.  Finally run the Minimum Bounding Geometry to find out each turtles home range (convex hull).  https://pro.arcgis.com/en/pro-app/tool-reference/data-management/minimum-bounding-geometry.htm  



  




      
      

