import numpy as np
import urllib.request as rq
import json
import arcpy
import ntpath

turtleID = arcpy.GetParameterAsText(0)
fc = arcpy.GetParameterAsText(1)
chfc = arcpy.GetParameterAsText(2)

out_path = ntpath.dirname(fc)
out_name = ntpath.basename(fc)

spatial_reference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(out_path, out_name, "Polyline", "", "", "", spatial_reference)
arcpy.AddField_management(fc, "TurtleID", "Long")

url = 'http://geo.conserveturtles.org/Tracking/GetTurtleLocationsByIdAsJson?id={}'.format(turtleID)
f = rq.urlopen(url)

turtledata = json.load(f)

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@", "TurtleID"])
pointsList = []
for turtleLocation in turtledata:
    x = turtleLocation["Lng"]
    y = turtleLocation["Lat"]
    pointsList.append(arcpy.Point(x,y))
                      
array = arcpy.Array(pointsList)
                      
myshape = arcpy.Polyline(array, spatial_reference)

cursor.insertRow([myshape, turtleID])

del cursor

arcpy.MinimumBoundingGeometry_management(fc, chfc, "CONVEX_HULL")

