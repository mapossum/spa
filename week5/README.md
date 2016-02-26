#Lecture
##Week 5 – Python in ArcGIS (arcpy)
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
2. ArcPy
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
3. Readings for you:
  1. http://downloads2.esri.com/ESRIpress/images/224/PYTHON_sample-ch5.pdf
  2. http://resources.arcgis.com/en/help/main/10.2/index.html#/What_is_geoprocessing/002s00000001000000/
  3. http://resources.arcgis.com/en/help/main/10.2/index.html#/What_is_Python/002z00000001000000/
  4. http://resources.arcgis.com/en/help/main/10.2/index.html#/What_is_ArcPy/000v000000v7000000/
  
 Video:  https://www.youtube.com/watch?v=Rkg039p7Veo#t=10666
 
  
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

You also have one question to answer in this lab.  What if the land use and/or census data did not fall completly within a TAZ unit but sometimes overlapped and had portions in two different TAZ units?  How would this change which GIS operations we would use?
      
      
      

