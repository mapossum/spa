import math, urllib
import urllib.parse
import urllib.request

def getaddresslocation(address):
    params = urllib.parse.urlencode({'SingleLine': address, 'f': 'json'})
    f = urllib.request.urlopen("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?%s" % params)
    loc = eval(f.read())
    return (loc['candidates'][0]['location']['x'], loc['candidates'][0]['location']['y'])

cities = ["Hattiesburg, MS", "Jackson, MS", "Poplarville, MS", "Hattiesburg, MS"]

import arcpy
arcpy.env.overwriteOutput = True

out_path = r"C:\temp\M7"
out_name = "Polygon.shp"
fc = r"{}/{}".format(out_path,out_name)
spatial_reference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(out_path, out_name, "Polygon", "", "", "", spatial_reference)

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
pointsList = []
for city in cities:
    x , y = getaddresslocation(city)
    pointsList.append(arcpy.Point(x,y))
                      
array = arcpy.Array(pointsList)
                      
myshape = arcpy.Polygon(array, spatial_reference)

cursor.insertRow([myshape])

del cursor
