#Lecture
##Meeting 7 - Working with GIS data and Functions
####Today we will continue to discuss making toolboxes from scripts.  We will discuss a few more items helpful to creating script tools.  


Link to script tool help:
http://desktop.arcgis.com/en/arcmap/10.4/analyze/creating-tools/adding-a-script-tool.htm
where to save items
in_memory workspace
preprocessing anything in your script that is always the same each time the tool is run
feature set and record set
select tool

#Lab

Exercise – Part of Exam 1
You will write a python script and implement it as a toolbox.  Our goal is the identification of areas suitable for a park development.  We want to make our toolbox flexible so that it allows for some varying of the inputs.  We will be working with data from the Marine on St. Croix area. Your job is to identify areas suitable for a 100 hectares (ha) park. The basic criteria are:
1) Build only on private land in Minnesota 
2) Slope less than or equal to a user specified value in degrees (This will be something the user will select in the toolbox).  You must restrict the value to a number between 1 and 10 degrees. 
3) The entire area needs to be within a user specified distance of a road (This will be something the user will select in the toolbox).   This number should be restricted to a number between 10 and 1000 m (1 km)
4) Must be more than a user specified distance from Lakes, streams, or rivers features.  (This will be something the user will select in the toolbox).   This number should be restricted to a number between 10 and 1000 m (1 km).
5) No building on any wetlands 
6) Individual polygons for final areas must be larger than a user specified area (in hectares)  You will apply this last.  This will require a Dissolve.
The model will basically prepare each data dataset from 1-3 and then intersect them.  After you prepare 4 and 5 you will erase those values.  Finally, you will dissolve and select only those areas that meet the area criteria.  
Think about which tasks can be done before hand.  Go ahead and process those, they do not need to be part of your script.  
You need to turn in a toolbox, and any data you preprocess in a file geodatabase. 
This exercise constitutes 3/5 of your grade for exam 1.  I will also post a written portion of the exam on Canvas which will also be take home and open notes.  You have until March 22th to complete this exercise and the written portion of the lab.

Explanation of Layers:
You are provided with the following data layers. 
1. All layers are in NAD83, UTM zone 15 coordinates, meters, and elevations in meters. Remember, there 10,000 square meters in each hectare. 
  1. MARON_slopePolygons - Polygons of the Slope in Degrees.  Slope field is the field you want to use. 
  2. MAR_BD - A polygon shapefile of major municipal regions from a USGS digital line graph. Ownership codes are in the item MODN_ID Codes 1, 7, and 8 are Wisconsin, 3 is private land in Chisago County, 9 private land in Washington County, and 2, 4, 5, 6, 10, and 11 either public land or within the borders of Marine on St. Croix. 
  3. MAR_HYD - A polygon shapefile, hydrologic features, from a USGS digital line graph.  Lakes, rivers, and ponds are represented as polygons 
  4. MAR_WET - A polygon shapefile of wetlands with item "attribute", giving USFWS wetlands type.  A value for Attribute of OUT contains no data and a value of ‘U’ is upland (i.e. not wetland)– don’t use these areas.  Use all the other areas as wetland. 
  5. MAR_RD - A line shapefile identifying road locations in the study area.

Video Link - Part 1: https://youtu.be/MSPdkH6hV0k
Video Link - Part 2: https://youtu.be/67cxnPirHRQ




      
      

