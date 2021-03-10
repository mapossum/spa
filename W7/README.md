#Lecture
##Meeting 7 - Working with Vector GIS Data with Python I

Much of the material for the lecture comes from PS4AGSPro Chapter 6,7,8 
I covered a signficant part of chapter 6 last week.  I am not really going to chapter 7 much.  Today we will mostly focus on Chapter 8 from PS4AGSPro.
We won't meet next week (I will post an exam and this weeks assignment will be longer than usual.
Short Test Review - Open everything - Ability to open test and enter test 10 times - Ask me questions.


1.  What is GIS (Vector) Data? 
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
  3. Converting Vector Data from / to Numpy arrays (if we get to it).
    1. Numpy
      1. What is an array?  https://docs.scipy.org/doc/numpy/index.html
      2. Array functions and utilites.
        1. Create Arrays: https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html
        2. Array Functions: https://docs.scipy.org/doc/numpy/reference/index.html
    2. FeatureClassToNumPyArray and TableToNumPyArray
    3. NumPyArrayToTable and NumPyArrayToFeatureClass
    4. ExtendTable

	
#Lab 

Here is your assignment.

1) Complete S4AGSPro Chapter 6 excerise and turn in the script(s).
 a. Text: https://southernmiss.maps.arcgis.com/home/item.html?id=cef0aa5df9c54993a6c1cb1dfec5f553  
 b. Data: https://southernmiss.maps.arcgis.com/home/item.html?id=3df07f29a0844d62af4338c52a40fda9
 
2) Complete S4AGSPro Chapter 7 excerise and turn in the script(s).
 a. Text: https://southernmiss.maps.arcgis.com/home/item.html?id=2a6a6a167ae94cdabc0fe8aa244744dc  
 b. Data: https://southernmiss.maps.arcgis.com/home/item.html?id=c75cce6b2ecd4ccb8a68638475c73201

3) Complete S4AGSPro Chapter 8 excerise and turn in the script(s).
 a. Text: https://southernmiss.maps.arcgis.com/home/item.html?id=0cad298208984ae4b3c3f7718195c174  
 b. Data: https://southernmiss.maps.arcgis.com/home/item.html?id=ea906d3a31d54824a1930806a0cfb59e 
 
4) Write a script that takes the tornado data and adds a new field called "Month" That is a string field (You can do this by running a toolbox in ArcGIS.  Then in your script, convert the values in the mo field from an integer to a string representation of the month (1 = "January", 2 = "February" etc) and stores them in the "Month" Field string you created.  Select a state (does not matter which one).  Select only the tornados in that state using an SQL statement and the "st" field.  Finally use the tool SummaryStatistics to create a table of the number of tornados each month for that state and use pandas to create a bar chart of the same information.  






  




      
      

