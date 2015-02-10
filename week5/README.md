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
 
  
#Lab Assignment
##Exercise #5 – Using ArcGIS to Model Growth

####Do the following assignment:

We have some data included in this lab.  The data consists of 4 different sets:

1. Census data
2. Transportation Analysis Zone Units (TAZ)
3. Land Use Data
4. Build Out Factor Table (CSV - TextFile)
5. Land Use Multipliers (TXT - TextFile)

The script you will create will calculate the population for each TAZ.  TAZ zones are defined as a group of census blocks so you can depend on a number of census blocks existing entirely within a TAZ zone (i.e. census blocks don't cross TAZ borders).
The land use data also is derived from census data so it does not cross borders either.  This is the equation for calculating population growth by TAZ zone:

Within Each TAZ there are multiple land uses.  Each land use contributes a factor to the overall growth for that TAZ as follows:

Land Use Factor  = Buildout * Acres * LandUseMultiplier * population growth multipler

The population growth multipler is:

population growth multiplier = Population / Households (Occupied Dwelling Units)

The Total population change is the total of all the land use factors

The solution will involve getting all the data into a table in columns and then adding those columns up.








Name the script W_X_Y_Z.py 

where :
* W is your last name, 
* X is your first name, 
* Y is the Exercise number (in this case 1) and 
* Z is the script number (the first is 1 then second is 2 and so on). 


Thus for the first script to turn in, I would name the file Raber_George_5_1.py

You will turn in 1 script for this exercise.
      
      
      

