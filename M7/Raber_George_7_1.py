import numpy as np
import urllib.request as rq
import json
import arcpy
arcpy.env.overwriteOutput = True

out_path = r"C:\temp\M7"
out_name = "TurtleTracks.shp"
fc = r"{}/{}".format(out_path,out_name)
spatial_reference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(out_path, out_name, "Polyline", "", "", "", spatial_reference)

#You want Everthing below here in a loop
#Create Turtle Data by asking for a turtle's track based on ID
turtleID = 1
url = 'http://geo.conserveturtles.org/Tracking/GetTurtleLocationsByIdAsJson?id={}'.format(turtleID)
f = rq.urlopen(url)

turtledata = json.load(f)

#You will need an if statement to skip all this if the Turtle data is empty
#Also to get full credit you need to save the Turtle ID into the Id field
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
pointsList = []
for turtleLocation in turtledata:
    x = turtleLocation["Lng"]
    y = turtleLocation["Lat"]
    pointsList.append(arcpy.Point(x,y))
                      
array = arcpy.Array(pointsList)
                      
myshape = arcpy.Polyline(array, spatial_reference)

#To get full credit insert the Turtle ID here.
cursor.insertRow([myshape])

#Except this 
del cursor

#Now run Minimum Bounding Geometry on the dataset to get a new dataset that is the convex hull of all the turtle tracks.
arcpy.MinimumBoundingGeometry_management(inFeatures, outFeatureClass, "CONVEX_HULL", "NONE")
