#Lecture
##Meeting 7 - Working with Vector GIS Data with Python I


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
    1. Search
    2. Insert
    3. Update
  3. Converting Vector Data from / to Numpy arrays.
    1. Numpy
      1. What is an array?  https://docs.scipy.org/doc/numpy/index.html
      2. Array functions and utilites.
        1. Create Arrays: https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html
        2. Array Functions: https://docs.scipy.org/doc/numpy/reference/index.html
    2. FeatureClassToNumPyArray and TableToNumPyArray
    3. NumPyArrayToTable and NumPyArrayToFeatureClass
    4. ExtendTable

	
Videos:
https://youtu.be/hWzcEoD9HzI <br>
https://youtu.be/ttYsvjtw4nQ

Test Review:
https://youtu.be/GOtCAUANWkI

#Lab 

Here is your assignment.

1) Write a script that takes the tornado data and adds a new field called "Month" That is a string field.  Then in your script, convert the values in the mo field from an integer to a string representation of the month (1 = "January", 2 = "February" etc) and stores them in the "Month" Field string you created.






  




      
      

