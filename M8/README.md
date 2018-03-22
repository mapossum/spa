#Lecture
##Meeting 8 - Working with GIS data 

1.  What is GIS Data? http://desktop.arcgis.com/en/arcmap/latest/analyze/python/reading-geometries.htm
  1. Points, Lines, Polygons  http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/geometry.htm
    1. What is a Point?
    2. What is a Line?
    3. What is a Polygon?
  2. Table Data
  3. Linked together
  4. Raster Data (We will talk more about that in a couple weeks)
2.  What can GIS systems do with GIS data?
  1. GIS operations.
    1. Examples
      1. Union
      2. Interset
      3. Buffer
      4. Difference
	  5. Find Areas
	  6. Find Lengths
	  7. Find Distances
3. Implmenting in Arcpy
  1. The data access module (da) - http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-data-access/what-is-the-data-access-module-.htm
  2. Cursors
    1. Search
    2. Insert
    3. Update
	
Vid 1: https://youtu.be/6G6iblph_aA
Vid 2: https://youtu.be/t2XfuQrKvi4

#Lab 

Here is your assignment.

Landscape metrics are statistics that can be caluclated for polygon shapes (patches) that can be utilized in a variety of applications.  
These statisitics are meant to be able to discover patterns in different types of patches for quantative comparison.  
Shape metrics represents a collection of unitless metrics that describe the geometric
complexity and/or compactness of patch shapes and quantify landscape configuration in terms of
geometric complexity at the patch, class, and landscape levels. Most of these shape metrics are
based on perimeter-area relationships. Some of the common metrics in this group include the
following:

1. Perimeter-area ratio (PARA) – simple ratio of patch perimeter to area, in which patch shape
is confounded with patch size; holding shape constant, an increase in patch size will cause a
decrease in the perimeter-area ratio. 
2. Shape index (SHAPE) – normalized ratio of patch perimeter to area in which the complexity
of patch shape is compared to a standard shape (such as a square) of the same size (PARA / PARA of Square of the same area).this alleviates
the size dependency problem of PARA.
3. Related circle of same area (SCIRCLE) - another method of assessing shape based on the
ratio of patch perimeter to the perimeter of a circle of the same area. (This is similar to Shape Index, except for using a circle instead of a square).
4. Related circumscribing circle (CIRCLE) – another method of assessing shape based on the
ratio of patch area to the area of the smallest circumscribing circle; providing a measure of
overall patch elongation. A highly convoluted but narrow patch will have a relatively low
related circumscribing circle index due to the relative compactness of the patch. Conversely,
a narrow and elongated patch will have a relatively high circumscribing circle index. This
index may be particularly useful for distinguishing patches that are both linear (narrow) and
elongated.
5. Fractal dimension index (FRAC) – another normalized shape index based on perimeter-area
relationships in which the perimeter and area are log transformed (We won't calculate this one).

The metrics have many applications in both envorimental, biological and social studies.  For example:

1. The shape of landscape patches (land cover) can influence habitats and the ability of certain species to colonize and grow.
2. The shape of patches can be used to determine what an object is by a computer alogrithm.  Agricultral fields, and meadows look simmilar spectrally, but often have different shapes.
3. The shapes of municiple boundaries, voting districs and other arbitrary social units especially over time can be an important cultural and social indicator. 

1) Your task for this lab is write a program that takes as input a shapefile, and adds a field for each of the first three metrics discussed above.  Then populates the appropriate value into the field (you should have 3 added fields).


Use the accompanying cities of Mississippi GIS file to test your program.





  




      
      

