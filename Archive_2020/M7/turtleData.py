import numpy as np
import urllib.request as rq
import json

turtleID = 1
url = 'http://geo.conserveturtles.org/Tracking/GetTurtleLocationsByIdAsJson?id={}'.format(turtleID)
f = rq.urlopen(url)

turtledata = json.load(f)
#First Turtle Location
print(turtledata[0])

import arcpy
arcpy.env.overwriteOutput = True

out_path = r"C:\temp\M7"
out_name = "TutleTracks.shp"
fc = r"{}/{}".format(out_path,out_name)
spatial_reference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(out_path, out_name, "Polyline", "", "", "", spatial_reference)

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
pointsList = []
for city in cities:
    x , y = getaddresslocation(city)
    pointsList.append(arcpy.Point(x,y))
                      
array = arcpy.Array(pointsList)
                      
myshape = arcpy.Polyline(array, spatial_reference)

cursor.insertRow([myshape])

del cursor
