import arcpy

#aprx = arcpy.mp.ArcGISProject("CURRENT")
aprx = arcpy.mp.ArcGISProject(r"C:\courses\spa\W10\PS4AGS_Ex11\Austin.aprx")
print(aprx.documentVersion)
print(aprx.filePath)


maps = aprx.listMaps()

print(maps[1].name)

del aprx
