import arcpy

#aprx = arcpy.mp.ArcGISProject("CURRENT")
aprx = arcpy.mp.ArcGISProject(r"C:\courses\spa\W10\PS4AGS_Ex11\Austin.aprx")
print(aprx.documentVersion)
print(aprx.filePath)


maps = aprx.listMaps("Austin*")

print(len(maps))
print(maps[0].name)

del aprx
