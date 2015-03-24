#Lecture
##Week 9 - Working with GIS data using Open Source Libraries
#### More on Accessing GIS data through Python
###### Today we will use a couple external libraries to do things we have already done using different tools. 

1. Shapely - http://toblerity.org/shapely/manual.html
  1. GEOS
  2. Do Shape things
    1. Union
    2. Interset
    3. Buffer
    4. Difference
2. Fiona - http://toblerity.org/fiona/manual.html
  1. GDAL & OGR (Actually have their own python bindings, but they were not designed for Python so they are harder to use, but more powerful).
    1. Sample script for adding fields (Fiona only does read and write, no adding field or changing data)
  2. Open Shapefiles and Read through them
  

#Lab 

Here is your assignment (You have two weeks to finish this assignment).

Redo the last lab (listed below again) but this time do not use arcpy at all.

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
of patch shape is compared to a standard shape (square) of the same size, thereby alleviating
the size dependency problem of PARA.
3. Related circumscribing circle (CIRCLE) – another method of assessing shape based on the
ratio of patch area to the area of the smallest circumscribing circle; providing a measure of
overall patch elongation. A highly convoluted but narrow patch will have a relatively low
related circumscribing circle index due to the relative compactness of the patch. Conversely,
a narrow and elongated patch will have a relatively high circumscribing circle index. This
index may be particularly useful for distinguishing patches that are both linear (narrow) and
elongated.
4. Related circle of same area (SCIRCLE) - another method of assessing shape based on the
ratio of patch perimeter to the perimeter of a circle of the same area. (This is similar to Shape Index, except for using a circle instead of a square).
5. Fractal dimension index (FRAC) – another normalized shape index based on perimeter-area
relationships in which the perimeter and area are log transformed (We won't calculate this one).

The metrics have many applications in both envorimental, biological and social studies.  For example:

1. The shape of landscape patches (land cover) can influence habitats and the ability of certain species to colonize and grow.
2. The shape of patches can be used to determine what an object is by a computer alogrithm.  Agricultral fields, and meadows look simmilar spectrally, but often have different shapes.
3. The shapes of municiple boundaries, voting districs and other arbitrary social units especially over time can be an important cultural and social indicator. 

1) Your task for this lab is write a program that takes as input a shapefile, and adds a field for each of the first four metrics discussed above.  Then populates the appropriate value into the field (you should have 4 added fields).
2) Also output a new shapefile that contains the difference between the smallest circumscribing circle and the area of the input polygon, and another shapefile that contains the circles that are the same area as the inputs.

The circle.py script, already contains code to calculate the smallest circumscribing circle.  Go ahead and use this rather than creating your own.
You will need to find the circle and square of the same area as each of the input polygons.

Use the accompanying cities of Mississippi GIS file to test your program.





  




      
      

