#Lecture
##Meeting 9 - Working with GIS data - Cont. Writing Geometries.
####Today we review GIS Data structures and talk about how they can accessed programattically.

Writing Geometries

#Lab 

Here is your assignment

From last week:

1) Build on the script from last week and output a new shapefile that contains the smallest circumscribing circle and the area of the input polygon.

The SEC.py script, already contains code to calculate the smallest circumscribing circle (function is called make_circle).  Go ahead and use this rather than creating your own.  It will be easiest to start by copying the orginal feature class then replacing the cities with the smallest circumscribing circle.  You should include a new field that is the ratio of the area to the city to the area of the circle.

2) Write a python program that does the following:
Take a point shapefile that has contains two fields.  In our case one will be called "Animal" and one field called "Time".  
The Point shapefile represents animal movements acquired using a GPS collar.  
1) You must create a line shapefile that contains one line per animal representing the movements of that animal from the earliest time to the latest time.
2) Your program should also create a polygon shapefile that represents the animal’s home range.  The home range will be defined as the polyline shapefile you create buffered by 0.1 km.
3) Your program should also find the amount of each animal's home range that is within each feature of another dataset called "Parks". (Find the amount of each home range that is within a park (Think GIS Intersect)).

Use the accompanying point GIS shapefile to test your program.

You will turn in 2 programs for this week.

New Video:  https://youtu.be/L9sFyJbdjm4

New Lab Video:  https://youtu.be/RPtMH-VizvE

Old Video: https://www.youtube.com/watch?v=UMyzk9mzY68



  




      
      

