import arcpy

#aprx = arcpy.mp.ArcGISProject("CURRENT")
aprx = arcpy.mp.ArcGISProject(r"G:\courses\spa\W10\PS4AGS_Ex11\Austin.aprx")
print(aprx.documentVersion)
print(aprx.filePath)


maps = aprx.listMaps()
for m in maps:
    print(m.name)
    m.name = "Austin " + m.name

#print(aprx.activeMap.name)

#aprx.activeMap.name = "Region"
aprx.save()

del aprx
