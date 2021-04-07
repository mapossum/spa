import arcpy

#aprx = arcpy.mp.ArcGISProject("CURRENT")
aprx = arcpy.mp.ArcGISProject(r"G:\courses\spa\W10\PS4AGS_Ex11\Austin.aprx")


maps = aprx.listMaps()
for m in maps:
    print("Map: " + m.name)
    lyrs = m.listLayers()
    for lyr in lyrs:
        print(lyr.name, lyr.dataSource, lyr.isFeatureLayer )

print(" ")
del aprx
