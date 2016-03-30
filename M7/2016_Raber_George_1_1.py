import arcpy
from arcpy import env

arcpy.env.overwriteOutput = True
out_path = r"C:\temp\m7"
out_name = "tracks.shp"
geometry_type = "POLYLINE"
template = r"C:\temp\m7\GPS_points.shp"
trackout = r"C:\temp\m7\tracksBuffer.shp"
fields1 = ["Shape@XY", "Animal"]
fields2 = ["Shape@", "Animal"]

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template)

cursor1 = arcpy.da.SearchCursor(template, fields1)
cursor2 = arcpy.da.InsertCursor(out_path + r"\\" + out_name, fields2)

previousanimal = -1
listofPoints = []
for pt in cursor1:
    if (previousanimal == -1):
        previousanimal = pt[1]
    animal = pt[1]
    coord = pt[0]
    print animal, previousanimal, coord
    if previousanimal != animal:
        print "DO the stuff"
        array = arcpy.Array(listofPoints)
        polyline = arcpy.Polyline(array)
        newrow = cursor2.insertRow((polyline,previousanimal))
        listofPoints = []
    listofPoints.append(arcpy.Point(coord[0], coord[1]))
    #Check to see if animal is the same as last time through the loop
    #If animail is different create a new polyline and put it in the output file (tracks).
    previousanimal = animal

print "DO the stuff"
array = arcpy.Array(listofPoints)
polyline = arcpy.Polyline(array)
newrow = cursor2.insertRow((polyline,previousanimal))
listofPoints = []    

del cursor1, cursor2


arcpy.Buffer_analysis(out_path + r"\\" + out_name, trackout , "100")


#Run buffer Tool

#Run intersect or Union tool
#Create Feild for Area
#Calculate Field Area with area inside 

print "done"
