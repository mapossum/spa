#Lecture
##Meeting 4 – Dictionaries and External Modules, Python in ArcGIS (arcpy)
####Today we will introduce and discuss arcpy, a module for interacting with ArcGIS:

1. Dictionaries – Are a data type that is like a list, but the index can be almost any other non sequence type (although it is typically a string)
  1. Sometimes called hashtables or associative arrays.
  2. Consist of a key and a value.
    1. Keys must be unique
    2. Values can be any of any type
2. Quick Review of what we have learned so far:
  1. Programming what is it and why are we doing it?
  2. Data types and Variables
  3. Program flow
    1. Making decisions (testing conditions and branching)
    2. Looping
  4. Functions
  5. Classes and Objects
  6. Methods and Properties
3. Modules
  1. Just a group of code that does things.
  2. Like functions, they can serve to organize your code better.
  3. You can write your own, but we usually won't for this course.  (If it helps you though go ahead and do it)
4. Classes and Objects
  1. We've already been using these
  2. What is a class and what is an object
  3. How do you create a class? (Not going to really cover in this class).
  4. How do you use a class (How do you create an object).
  5. Again, in this class we will mostly be consumers of classes and objects other's have written, but if it helps you to orgainze things go ahead and create your own.
5. ArcPy
  1. ArcGIS Pro has python built right in.
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
6. External Modules (often use custom classes they have included)
  1. arcpy (Interacting with ArcGIS)
  2. gdal (Using Open Source GIS tools)
  3. psycopg (Interacting with PostGres and PostGIS, doing GIS in a Database)
  3. numpy (Arrays) *
  4. scipy (Scientific analysis of Arrays) *
  5. flask and django (Web framworks)
  6. Tkinter (GUI design)
  7. matplotlib (plots and graphs) *
  9. seaborn (Advanced Statistical plots and graphs based on matplotlib).
  8. Pillow (Image Processing)
  * means is included with ArcGIS install
6. Readings for you:
  1. https://pro.arcgis.com/en/pro-app/help/analysis/geoprocessing/basics/what-is-geoprocessing-.htm
  2. https://pro.arcgis.com/en/pro-app/arcpy/get-started/installing-python-for-arcgis-pro.htm
  3. https://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm

 2019 Lecture Video: https://youtu.be/hvNVtX1K_Eg
 2019 Lab Video: https://youtu.be/murtnYG94HU

 2018 Lecture Video: https://youtu.be/KC13FIYA2Ns
 2018 Video for Lab: https://youtu.be/E79MKf_L-4s
 Old Video:  https://www.youtube.com/watch?v=AGvjPEYvFNo
 
  
#Lab Assignment
##Exercise #4 – Using ArcGIS to run a simple model

####Do the following assignments:

1. Write a program that reads a list of cities from a file, creates and prints the contents of a dictionary where the keys are the city names and the values are the locations as a x,y pairs (as tuple or list).  The file location.py contains a function that takes an text location and returns a dictionary with the location as x,y.  The file citiesSubset contains a file with a list of cities you can use for testing.


We have some data included in this lab.  The data consists of 2 different sets:

* Census data
* Watersheds

2. You will create a simple script that calcuates how many people live in each watershed.  Since the watershed boundaries and the census boundaies do not match up you will use GIS to break apart (overlay) and assign people to each watershed.  We will tackle this in a simple way.  First do the overlay (we did it using the Identity tool in class), then do a dissolve.  Use a unique field for the dissolve field (e.g. HUC_8) and summarize based on the population (e.g. P0010001)  based on the percentage of area a particular tract has in each watershed. Your output will be the total number of people in each watershed, but it is just an estimate as cencus tracts that strattle watershed boundaries will be double counted.

Name the script W_X_Y_Z.py 

where :
* W is your last name, 
* X is your first name, 
* Y is the Exercise number (in this case 1) and 
* Z is the script number (the first is 1 then second is 2 and so on). 

Thus for the first script to turn in, I would name the file Raber_George_4_1.py

You will turn in 1 script for this exercise.
  
      
      

