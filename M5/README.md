#Lecture
##Meeting 5 – Python in ArcGIS (arcpy)
####Today we will introduce and discuss arcpy, a module for interacting with ArcGIS:

1. Quick Review of what we have learned so far:
  1. Programming what is it and why are we doing it?
  2. Data types and Variables
  3. Program flow
    1. Making decisions (testing conditions and branching)
    2. Looping
  4. Functions
  5. Classes and Objects
  6. Methods and Properties
2. Modules
  1. Just a group of code that does things.
  2. Like functions, they can serve to organize your code better.
  3. You can write your own, but we usually won't for this course.  (If it helps you though go ahead and do it)
3. Classes and Objects
  1. We've already been using these
  2. What is a class and what is an object
  3. How do you create a class?
  4. How do you use a class (How do you create an object).
  5. Again, in this class we will mostly be consumers of classes and objects other's have written, but if it helps you to orgainze things go ahead and create your own.
4. ArcPy
  1. ArcGIS 10 has python built right in.
  2. arcpy module is for making requests to the arcgis toolboxes (Geoprocessing)
    1. Importing arcpy
    2. Using Tools
    3. Using Functions
    4. Environmental Options:
    5. env object – allows you to set or change default processing options for geoprocessing.
      1. cellSize
      2. extent
      3. overwriteOutput
    6. Describe
5. External Modules (often use custom classes they have included)
  1. arcpy (Interacting with ArcGIS)
  2. gdal (Using Open Source GIS tools)
  3. psycopg (Interacting with PostGres and PostGIS, doing GIS in a Database)
  3. numpy (Arrays) *
  4. scipy (Scientific analysis of Arrays) *
  5. flask and django (Web framworks)
  6. Tkinter (GUI design)
  7. matplotlib (plots and graphs) *
  8. Pillow (Image Processing)
  * means is included with ArcGIS install
6. Readings for you:
  1. http://downloads2.esri.com/ESRIpress/images/224/PYTHON_sample-ch5.pdf
  2. http://desktop.arcgis.com/en/arcmap/latest/analyze/main/what-is-geoprocessing.htm
  3. http://desktop.arcgis.com/en/arcmap/latest/analyze/python/what-is-python-.htm
  4. http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy/what-is-arcpy-.htm

 2018 Lecture Video: https://youtu.be/KC13FIYA2Ns
 2018 Video for Lab: https://youtu.be/E79MKf_L-4s
 Old Video:  https://www.youtube.com/watch?v=AGvjPEYvFNo
 
  
#Lab Assignment
##Exercise #5 – Using ArcGIS to run a simple model

####Do the following assignment:

We have some data included in this lab.  The data consists of 2 different sets:

1. Census data
2. Watersheds

You will create a simple script that calcuates how many people live in each watershed.  Since the watershed boundaries and the census boundaies do not match up you will use GIS to break apart (overlay) and assign people to each watershed based on the percentage of area a particular tract has in each watershed.  For example if 100 people live in a tract and 80% of the area of that tract falls in a watershed then 80 people will be counted for that watershed.  Your output will be the total number of people in each watershed.

Name the script W_X_Y_Z.py 

where :
* W is your last name, 
* X is your first name, 
* Y is the Exercise number (in this case 1) and 
* Z is the script number (the first is 1 then second is 2 and so on). 

Thus for the first script to turn in, I would name the file Raber_George_5_1.py

You will turn in 1 script for this exercise.
  
      
      

