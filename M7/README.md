#Lecture
##Meeting 6 - Working with Vector GIS Data with Python I


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

	
Videos:

#Lab 

Here is your assignment.

1) Write a script that takes the tornado data and adds a new string field called month.  Then using the Update and/or the Search Cursor it puts in the proper month string into the field ("January" for 1, "February" for 2 and so on).  You can base this on the example we did in class where we created a new field and calculated a new value based on the existing magnitude value.





  




      
      

